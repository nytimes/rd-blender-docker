"""
A script to automatically builds and tags all the Dockerfiles in dist folder

Written by juniorxsound <https://orfleisher.com>
"""

import os
import json
import shutil
import subprocess

if __name__ == "__main__":

    # @todo should be a CLI argument
    output_folder = "./dist/"

    # Open the manifest file and start generating Dockerfiles
    with open("./manifest.json", "r") as r:
        manifest = json.load(r)

        for image in manifest["images"]:
            # Check if folder exists first
            if os.path.exists(output_folder + image["tag"]):
                print("----------------------------------------------------------")
                print("🛠️ Building image nytimes/blender:{}".format(image["tag"]))

                # Build the Docker image
                os.system(
                    "docker build -q ./ -f {}/Dockerfile -t nytimes/blender:{}".format(
                        output_folder + image["tag"], image["tag"]
                    )
                )

                # Copy the README from root so it deploys to DockerHub
                if os.getenv("CI") != None:
                    print("Copying README to Dockerfile folder on CI so it deploys to Docker Hub\n")
                    shutil.copy2("./README.md", output_folder + image["tag"])

                print(
                    "✔️ Built and tagged image nytimes/blender:{}".format(image["tag"])
                )
                print("----------------------------------------------------------\n")
