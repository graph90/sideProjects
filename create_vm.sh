#!/bin/bash

read -p "Enter the VM name: " VM_NAME
read -p "Enter the disk size (e.g., 20G): " DISK_SIZE
read -p "Enter the amount of RAM (in MB, e.g., 4096): " RAM
read -p "Enter the number of CPU cores (e.g., 2): " CPU_CORES
read -p "Enter the path to the Ubuntu ISO (default: ubuntu-24.04.1-desktop-amd64.iso): " ISO
ISO=${ISO:-ubuntu-24.04.1-desktop-amd64.iso}

echo "Creating virtual disk ${VM_NAME}.img with size ${DISK_SIZE}..."
qemu-img create -f qcow2 "${VM_NAME}.img" "${DISK_SIZE}"

if [ $? -ne 0 ]; then
    echo "Failed to create virtual disk. Exiting."
    exit 1
fi

echo "Running VM '${VM_NAME}' with ISO mounted for installation..."
qemu-system-x86_64 -m "${RAM}" -cdrom "${ISO}" -hda "${VM_NAME}.img" -boot d -enable-kvm -smp "${CPU_CORES}"

echo "Installation complete. To boot the VM without the ISO, run the following command:"
echo "qemu-system-x86_64 -m ${RAM} -hda ${VM_NAME}.img -enable-kvm -smp ${CPU_CORES}"
