# Run with Tilt, Debug with [`remote-pdb`](https://pypi.org/project/remote-pdb/)

This directory contains an example of how to wire your app for use with [`remote-pdb`](https://pypi.org/project/remote-pdb/)---though of course, you can use any debugger you like, as long as it exposes a port for connection. For more information on using remote debuggers with your Tilt setup, check out [our guide to Python debuggers](https://docs.tilt.dev/debuggers_python.html).

To see `remote-pdb` in action:

1. Call `tilt up` from this directory
2. Hit `localhost:8000`; the request will hang because the app hit a breakpoint. You'll know that the debugger is live and ready for connections when you see the following in the logs:
  ```
  CRITICAL:root:RemotePdb session open at 127.0.0.1:5555, waiting for connection …
  RemotePdb session open at 127.0.0.1:5555, waiting for connection …
  ```
3. In a separate terminal window, open a TCP connection to `localhost:5555`, e.g. via Netcat: `nc 127.0.0.1 5555`
4. Congrats, you've accessed the debugger! Poke around and inspect the system state. Type `c(ontinue)` to resume execution.
