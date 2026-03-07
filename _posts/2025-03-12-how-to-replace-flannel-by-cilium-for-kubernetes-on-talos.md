---
title: Setting Up Cilium on Talos in Proxmox
date: 2025-03-12 21:00:00 +0100
categories: [DevOps, Kubernetes]
tags: [kubernetes, talos, cilium, homelab] # TAG names should always be lowercase
description: Switching from Flannel to Cilium for enhanced networking
author: sofianlak
image:
  path: /assets/img/headers/flannel-to-cilium.png
---

> This article is for the setup of a new Kubernetes cluster with Talos. I am not here coverring how to cleanup your existing cluster for removing Flannel.
{: .prompt-info }

## **Introduction**

If you clicked on this article, it’s probably because you’re familiar with at least one of the four key technologies: Cilium, Kubernetes, Talos, or Proxmox. But for those who are curious or need a bit more context, let’s break it down.

-	**`Kubernetes`** is a container orchestrator designed to scale and manage containerized applications efficiently. It provides a rich set of APIs to handle deployments, networking, and more.
-	**`Talos`** is a lightweight, immutable Linux OS specifically built for running Kubernetes clusters. It simplifies cluster deployment by eliminating the need to manually install and configure Kubernetes components (which is usually done with kubeadm).
-	**`Proxmox`** is a powerful open-source virtualization platform that allows us to create and manage virtual machines.

Now, how do these pieces fit together? We’ll use Proxmox to create virtual machines, install Talos as the OS, and deploy a Kubernetes cluster on top of it.

**Wait, but what about Cilium?**

By default, Talos uses Flannel as the CNI (Container Network Interface) along with kube-proxy to handle networking. However, if you want more control, security, and observability in your Kubernetes networking, Cilium is the way to go. Cilium replaces kube-proxy and brings advanced networking features like eBPF-based security policies, high-performance networking, and deep observability.


## **Install Proxmox & Talos**

- **Ensure Proxmox is installed and configured**

I am assuming that you already have a Proxmox server ready. If not, you can get started by following the [Proxmox Getting Started Guide](https://www.proxmox.com/en/products/proxmox-virtual-environment/get-started){:target="\_blank"}.

- **Install talosctl on your local machine**

You can download talosctl on macOS and Linux via:

```shell
brew install siderolabs/tap/talosctl
```

or if you prefer this way:

```shell
curl -sL https://talos.dev/install | sh
```

- **Download the Talos ISO from the Talos Image Factory**

Get the Talos ISO from the [Talos Image Factory](https://factory.talos.dev){:target="\_blank"} Ensure that during the system extensions selection, you choose the QEMU agent to enable communication between Proxmox and your cluster.

- **Upload the ISO to Proxmox and create VMs as per the standard Talos installation guide**

Upload the Talos ISO to Proxmox and create virtual machines as per the standard Talos installation guide. 

Follow the steps up [here](https://www.talos.dev/v1.9/talos-guides/install/virtualized-platforms/proxmox/?utm_source=chatgpt.com#upload-iso){:target="\_blank"} to “Upload ISO,” “Create VMs,” and “Start Control Plane Node,” then return here to continue with the core subject.


## **Remove Default CNI (Flannel) via patch.yaml**

As mentioned earlier, Talos installs Flannel by default for networking. 

To disable it and configure Talos to operate without any CNI initially, create a patch.yaml file with the following content:


```shell
cluster:
  network:
    cni:
      name: none
  proxy:
    disabled: true
```
{: file="patch.yaml" }


## **Generate Machine Configurations**


Okay now we will tackle the Talos configuration. 

When your controlplane and worker node are ready just start them in Promox, it will boot and generate your ip address (*if you have a DHCP if you don't follow the documentation for static IP [here](https://www.talos.dev/v1.9/talos-guides/install/virtualized-platforms/proxmox/?utm_source=chatgpt.com#without-dhcp-server){:target="\_blank"})*

- **Identify the IPs of your nodes and store them in environment variables**
```shell
export $CONTROL_PLANE_IP=***
export $WORKER_IP=***
```
- **Now, generate the Talos configuration files**
```shell
talosctl gen config talos-proxmox-cluster https://$CONTROL_PLANE_IP:6443 --output-dir _out --config-patch @patch.yaml
```
This will create the necessary YAML configurations in the _out/ directory and use our patch to not generate the CNI config.

- **Apply configuration for the control plane**
```shell
talosctl apply-config --insecure --nodes $CONTROL_PLANE_IP --file _out/controlplane.yaml
```

-  **Apply configuration for the worker node**
```shell
talosctl apply-config --insecure --nodes $WORKER_IP --file _out/worker.yaml
```

- **Now, set up talosctl to interact with the cluster**
```shell
export TALOSCONFIG="_out/talosconfig"
talosctl config endpoint $CONTROL_PLANE_IP
talosctl config node $CONTROL_PLANE_IP
```

- **Run the bootstrap command to initialize the Talos Kubernetes control plane**
```shell
talosctl bootstrap
```

- **Finally, retrieve the Kubernetes configuration**
```shell
talosctl kubeconfig .
```

- **If you had already a KUBECONFIG file you can use this command**
```shell
export KUBECONFIG=$(pwd)/kubeconfig
```

<br>
Now, your machines will automatically reboot, and you just need to wait a few minutes for the Kubernetes components to be up and running.

## **Install Cilium**
Now you have a Kubernetes cluster running, but with no networking. Let’s install Cilium for networking! 

You can install Cilium using either the Cilium CLI or Helm.


### **Using Cilium CLI**

```shell
cilium install \
    --set ipam.mode=kubernetes \
    --set kubeProxyReplacement=true \
    --set securityContext.capabilities.ciliumAgent="{CHOWN,KILL,NET_ADMIN,NET_RAW,IPC_LOCK,SYS_ADMIN,SYS_RESOURCE,DAC_OVERRIDE,FOWNER,SETGID,SETUID}" \
    --set securityContext.capabilities.cleanCiliumState="{NET_ADMIN,SYS_ADMIN,SYS_RESOURCE}" \
    --set cgroup.autoMount.enabled=false \
    --set cgroup.hostRoot=/sys/fs/cgroup \
    --set k8sServiceHost=localhost \
    --set k8sServicePort=7445
```

### **Using Helm**


```shell
helm repo add cilium https://helm.cilium.io/
helm repo update

helm install \
    cilium \
    cilium/cilium \
    --version 1.15.6 \
    --namespace kube-system \
    --set ipam.mode=kubernetes \
    --set kubeProxyReplacement=true \
    --set securityContext.capabilities.ciliumAgent="{CHOWN,KILL,NET_ADMIN,NET_RAW,IPC_LOCK,SYS_ADMIN,SYS_RESOURCE,DAC_OVERRIDE,FOWNER,SETGID,SETUID}" \
    --set securityContext.capabilities.cleanCiliumState="{NET_ADMIN,SYS_ADMIN,SYS_RESOURCE}" \
    --set cgroup.autoMount.enabled=false \
    --set cgroup.hostRoot=/sys/fs/cgroup \
    --set k8sServiceHost=localhost \
    --set k8sServicePort=7445
```


After the installation, you can check if the Cilium components are up and running.

Now, you can explore Cilium! By following these steps, you’ve set up a Kubernetes cluster on Talos within Proxmox, using Cilium as your CNI to enable enhanced networking capabilities.

For more detailed information, refer to the [Talos Guide on Deploying Cilium CNI](https://www.talos.dev/v1.9/kubernetes-guides/network/deploying-cilium/){:target="\_blank"}.
