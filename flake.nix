{
  description = "Bubble Gum Simulator bot";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }: {
    packages.x86_64-linux.default = import ./shell.nix { inherit (nixpkgs) pkgs; };
  };
}
