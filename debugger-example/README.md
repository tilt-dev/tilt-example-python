# Run with Tilt, Debug with [`remote-pdb`](https://pypi.org/project/remote-pdb/)

This directory contains an example of how to wire your app for use with [`remote-pdb`](https://pypi.org/project/remote-pdb/), which is currently our recommended debugger for use with Tilt + Kubernetes (though of course, you can use any debugger you like, as long as it exposes a port for connection.) For more information on using remote debuggers with your Tilt setup, check out [our guide to Python debuggers](https://docs.tilt.dev/debuggers_python.html).

To see `remote-pdb` in action:

1. Clone this repo and call `tilt up` to run the app
2. Hit `localhost:8000`; the request will hang because the app hit a breakpoint
3. In a separate terminal window, open a TCP connection to `localhost:5555`, e.g. via Netcat: `nc 127.0.0.1 5555`
4. Congrats, you've accessed the debugger! Poke around and inspect the system state. Type `c(ontinue)` to resume execution.
