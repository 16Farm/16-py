# android-16-pc
a project i worked on to learn python.
<br>
<img src="https://cdn.discordapp.com/attachments/668875622822707203/785543285028421703/unknown.png">
# Comparison
- <b>why split the game versions?</b>
<br>
each API domain is different as well as the API port. some cases the API port has been different compared to the other version.
<br>
e.g. "3001" remained on global while japan changed to "443"
<br>
the solution to this was getting these initially before use from the endpoint "/ping" just like the game does.
<br>
they changed japans hypertext protocol from "HTTP" to "HTTPS" (explains the port change) which broke any bot that makes "HTTP" requests. (<a href="https://github.com/FlashChaser/Open-Source-Battle-Bot/blob/development/commands.py#L103">seen here</a>)
<br>
<br>
endpoints can also be changed on one version while the other remains on another version.
<br>
an example of this was when stamina refill endpoint was changed.
<br>
"/user/recover_act" -> "/user/recover_act_with_stone"
<br>
this broke flashchaser farmbot <a href="https://github.com/FlashChaser/Open-Source-Battle-Bot/commit/e16f31d4b96643716dae714aa616fd2ae7689d2b#diff-bca63731c9065cb6cbd3c1131c7e7c81">at the time</a>.
<br>
<br>
it's also to determine & send the correct version code for the game version in requests.
<br>
<br>
found by renzy on <a href="https://twitter.com/dbzspace/status/1106316112638210050">march 2019</a> they append a double MD5 hash to the app version sent to the servers.
<br>
this wasn't hard to fix just that we had to get it (at the time) by sniffing requests that included it or by Renzy's way- getting it from the updated app's "lib.so"
<br>
<br>

- <b>why split account OS?</b>
<br>
first reason was to send a proper request "User-agent"... all other bots were sending "Browser User-agents" instead of common User-agents used in "app code requests".
<br>
this also means they were sending 1 User-agent for every account used instead of switching between iOS or Android. which told their servers that they were just using "Firefox on Android". (<a href="https://github.com/FlashChaser/Open-Source-Battle-Bot/blob/development/commands.py#L87">seen here</a>)
<br>
<br>
another was to use the "X-Platform" header to tell their servers we really were using either iOS or Android.
<br>
without this would be a chance they reset all stones on the account for transferring to a different OS.
<br>
<br>
as of June 2020's app update they can split the app version to the corresponding device OS.
