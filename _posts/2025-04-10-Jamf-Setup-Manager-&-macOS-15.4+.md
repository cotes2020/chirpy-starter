# How changes to macOS 15.4 impact the use of Jamf Setup Manager

## Firstly, how has Setup Assistant changed in macOS 15.4? 

The main headline is that the `Location Services` pane now appears _**after**_ the user signs in.

Apple have provided admins the ability to configure which SA panes their clients display for many years with the [SkipKeys](https://developer.apple.com/documentation/devicemanagement/skipkeys) Configuration Profile payload.
MDMs often incorporate this into their ADE configuration options - in Jamf this is called _Prestage_.

Often, organisations limit the number of panes displayed to as few as possible, keeping `Location Services` enabled to ensure it's enabled without need for custom scripting or for admin permission to enable it when SA has completed.

## What does this mean for Setup Manager?

###### Well, that depends how you use Setup Manager...
If you're setting your `runAt` key to `enrolment` - as in, it installs, launches, and completes _during_ SA, you're going ot have to make changes to the Panes that are displayed so there's an pane displayed that is pending an action which Setup Manager can run on top of.

In the `enrolment` context, that's all Setup Manager is doing - running above a pane that hasn't yet been progressed past by a human action.
Most admins have reported that the `Terms and Conditions` pane is a suitable candidate for this as it runs _before_ user sign in.

If you want to find a different pane that would also work, an option could be to remove a device from _any_ prestage and note the panes you see _before_ you've created your account.


If you're setting your `runAt` key to `loginwindow` then you shouldn't need to make any changes to the panes that you display, but there are other challenges to be aware of if your organisation makes use of products like Jamf Connect, Xcreds, or similar, to create user accounts.
More details on that can be found in @scriptingosx's [post](https://github.com/jamf/Setup-Manager/discussions/96).


## Is there any best practice?

##### In short, no... 
How you use Setup Manager is entirely down to the requirements of your organisation or your personal preferences.

Given the impact these changes have brought about, it's evident that setting your `runAt` key to `loginwindow` could be a more robust option if there are future changes made to SA, but that comes with it's own challenges.

The only best practice advice given is test, test, and test again.
Oh, and make sure you join AppleSeed for IT if you're able to. You can get hands-on with Beta versions of macOS before they're released, and find solutions for your organisation before the GA release.
