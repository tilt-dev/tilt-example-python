# Run with Tilt, Debug with [`web-pdb`](https://github.com/romanvm/python-web-pdb)

This directory contains an example of how to wire your app for use with [`web-pdb`](https://github.com/romanvm/python-web-pdb). For more information on using remote debuggers with your Tilt setup, check out [our guide to Python debuggers](https://docs.tilt.dev/debuggers_python.html).

To see `web-pdb` in action:

1. Call `tilt up` from this directory
2. Hit `localhost:8000`; the request will hang because the app hit a breakpoint. You'll know that the debugger is live and ready for connections when you see the following in the logs:
  ```
  CRITICAL - Web-PDB: starting web-server on [podname]:5555...
  ```
3. In a new tab in your web browser, navigate to `localhost:5555`
4. Congrats, you've accessed the debugger! Poke around and inspect the system state. Type `c(ontinue)` to resume execution.
