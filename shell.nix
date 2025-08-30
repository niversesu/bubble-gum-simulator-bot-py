# shell.nix
{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.curl
  ];

  shellHook = ''
    echo "Welcome to the dev environment)"
  '';
}
