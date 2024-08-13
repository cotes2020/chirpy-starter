---
title: "Building a Reusable Sidebar in Rails with TailwindCSS and Heroicons"
date: 2024-03-25 08:00:00 -0500
categories: [Rails, TailwindCSS, Heroicons]
tags: [Entrepreneur, Créateur de contenu, Business starter]
image:
    path: /assets/img/headers/sidebar_rails.webp
    lqip: data:image/webp;base64,UklGRkAAAABXRUJQVlA4IDQAAAAQAwCdASoUAAsAPzmGu1OvKSYisAgB4CcJYwAAW+ll18AA/rniDRhs9sq0/4Ip9WfHYHAA

---

# Building a Reusable Sidebar in Rails with TailwindCSS and Heroicons

Creating a sidebar in a web application can be a daunting task, but with the power of TailwindCSS and Heroicons, it becomes both efficient and stylish. This post will guide you through building a reusable sidebar component in a Rails application using these modern tools, while keeping the code DRY (Don't Repeat Yourself).

## Prerequisites

Before getting started, make sure you have the following set up in your Rails application:

- **TailwindCSS** for styling.
- **Heroicons** for icons.

## Step-by-Step Guide

### 1. Create the Sidebar Link Partial

The first step is to create a partial for the sidebar links. This makes your code reusable and maintainable.

Create the file `app/views/layouts/components/_sidebar_link.html.erb` with the following content:

```erb
<li>
    <%= link_to path, class: "flex items-center space-x-3 px-3 py-2 text-sm font-medium text-gray-700 dark:text-neutral-200 rounded-lg #{'bg-gray-100 dark:bg-neutral-700' if current} hover:bg-gray-200 dark:hover:bg-neutral-600 transition-colors duration-200" do %>
        <%= heroicon icon, class: "h-5 w-5" %>
        <span><%= text %></span>
    <% end %>
</li>
```

This partial accepts four parameters: `path`, `icon`, `text`, and `current`.

### 2. Create the Sidebar Partial

Next, create a sidebar partial that uses the link partial for adding navigation links.

Create the file `app/views/layouts/_sidebar.html.erb` with the following content:

```erb
<div class="bg-white dark:bg-neutral-800 w-64 min-h-screen">
    <div class="p-4">
        <!-- Logo -->
        <%= link_to root_path, class: "flex items-center space-x-2" do %>
            <%= image_tag "logo.svg", alt: "Logo", class: "h-10 w-10" %>
            <span class="text-xl font-semibold text-gray-900 dark:text-white">App Name</span>
        <% end %>
        <!-- End Logo -->
    </div>

    <nav class="p-4 space-y-4">
        <ul class="space-y-2">
            <%= render 'layouts/components/sidebar_link', path: root_path, icon: 'home', text: 'Home', current: current_page?(root_path) %>
            <%= render 'layouts/components/sidebar_link', path: about_path, icon: 'information-circle', text: 'About', current: current_page?(about_path) %>
            <%= render 'layouts/components/sidebar_link', path: contact_path, icon: 'phone', text: 'Contact', current: current_page?(contact_path) %>
            <%= render 'layouts/components/sidebar_link', path: help_path, icon: 'support', text: 'Help', current: current_page?(help_path) %>
            <li>
                <%= form_with url: destroy_user_session_path, method: :delete, class: "inline" do %>
                    <button type="submit" class="flex items-center space-x-3 px-3 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-neutral-700 dark:text-neutral-200 dark:hover:text-white rounded-lg">
                        <%= heroicon "logout", class: "h-5 w-5" %>
                        <span>Sign Out</span>
                    </button>
                <% end %>
            </li>
        </ul>
    </nav>
</div>
```

This partial dynamically creates a sidebar with links by using the `_sidebar_link.html.erb` partial.

### 3. Render the Sidebar in Your Layout

Include the sidebar partial in your main layout file, usually located at `app/views/layouts/application.html.erb`:

```erb
<body>
    <%= render 'layouts/sidebar' %>
    <div class="flex-1">
        <%= yield %>
    </div>
</body>
```

## Benefits of This Approach

- Reusability: The sidebar link partial makes it easy to add or modify links without repeating code.
- DRY Principle: By using partials, the code remains organized and avoids unnecessary repetition.
- Responsive Design: TailwindCSS provides utility classes that ensure the sidebar is responsive and visually appealing.
- Consistent Icon Styling: Heroicons integrate smoothly with TailwindCSS classes for consistent icon styling.