{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python310     # or whichever Python version you want
    pkgs.python310Packages.requests
    pkgs.python310Packages.pyautogui
    pkgs.python310Packages.pyperclip
  ];

  shellHook = ''
    echo "Welcome to the Python dev environment!"
  '';
}
