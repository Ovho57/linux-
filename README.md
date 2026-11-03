# Kali Linux WSL Automated Installer

A command-line automation script for deploying a Kali Linux environment using the Windows Subsystem for Linux (WSL).

## Overview

This repository provides a streamlined script to automate the setup of Kali Linux on Windows. It eliminates manual configuration by validating administrative privileges, ensuring the WSL core engine is installed and updated, and pulling the official Kali Linux distribution directly from Microsoft's repositories.

## Prerequisites

* Windows 10 (Build 19041 or higher) or Windows 11.
* Hardware virtualization enabled in BIOS/UEFI.
* Terminal running with Administrator privileges.
* `curl` (pre-installed on modern Windows versions) or `wget`.

## Installation

Open **PowerShell** or **Windows Terminal** as an **Administrator**.

To install via `curl`, execute:

    curl -sL https://raw.githubusercontent.com/Ovho57/Kali-WSL-Installer/main/install.sh | bash

To install via `wget`, execute:

    wget -qO- https://raw.githubusercontent.com/Ovho57/Kali-WSL-Installer/main/install.sh | bash



## Execution Flow

The `install.sh` script executes the following sequence:

1. Validates elevated terminal permissions (`net session`).
2. Installs or updates the WSL core engine without triggering a default distribution installation (`wsl --install --no-distribution`).
3. Provisions the official Kali Linux distribution (`wsl --install -d kali-linux`).
4. Outputs the launch command upon successful completion.

## Usage

Once the script completes successfully, launch the environment from your terminal:

    wsl -d kali-linux

During the initial boot, you will be prompted to create a UNIX username and password.

## Security Note

This script relies exclusively on official Microsoft and Kali Linux distribution channels via the native `wsl` command-line interface. It does not download or execute third-party binaries, nor does it bypass native Windows security controls.
