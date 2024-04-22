#!/usr/bin/env python3

# Libraries
##############################################################################
import docker
import logging

from .helper_funcs import convert_size
##############################################################################

# Check Docker
##############################################################################
def check_docker_installed() -> bool:
    """
    Check if docker installed or running
    """
    try:
        client = docker.from_env()
        client.ping()
        return True
    except:
        return False
##############################################################################

# Docker Info
##############################################################################
def get_docker_info():
    # Check if installed or running
    if not check_docker_installed():
        return {
            "is_installed": False
        }

    try:
        # Connect to the Docker daemon
        client = docker.from_env()

        # Get Docker images
        images = client.images.list()

        # Get Docker containers
        containers = client.containers.list(all=True)

        # Get Docker volumes
        volumes = client.volumes.list()

        # Get Docker networks
        networks = client.networks.list()

        # Get Docker disk usage
        disk_usage = client.df()

        # Prepare Docker information
        docker_info = {
            "is_installed": True,
            "images": [],
            "containers": [],
            "volumes": [],
            "networks": [],
            "disk_usage": {
                "total_space": convert_size(disk_usage["LayersSize"])
            }
        }

        # Collect Docker image information
        for image in images:
            docker_info["images"].append({
                "image_id": image.id,
                "tags": image.tags,
                "size": convert_size(image.attrs["Size"]),
                "created": image.attrs["Created"],
                "labels": image.attrs["ContainerConfig"]["Labels"]
            })

        # Collect Docker container information
        for container in containers:
            docker_info["containers"].append({
                "container_id": container.id,
                "image": container.attrs["Config"]["Image"],
                "status": container.attrs["State"]["Status"],
                "ports": container.attrs["NetworkSettings"]["Ports"],
                "networks": container.attrs["NetworkSettings"]["Networks"],
                "created": container.attrs["Created"],
                "labels": container.attrs["Config"]["Labels"]
            })

        # Collect Docker volume information
        for volume in volumes:
            docker_info["volumes"].append({
                "volume_name": volume.name,
                "mountpoint": volume.attrs["Mountpoint"],
                "created": volume.attrs["CreatedAt"],
                "labels": volume.attrs["Labels"]
            })

        # Collect Docker network information
        for network in networks:
            docker_info["networks"].append({
                "network_id": network.id,
                "name": network.name,
                "driver": network.attrs["Driver"],
                "created": network.attrs["Created"],
                "labels": network.attrs["Labels"]
            })

        return docker_info
    except Exception as e:
        # Log the error
        logging.error(e)
        return False
##############################################################################
