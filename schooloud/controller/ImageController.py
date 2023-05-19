from flask import jsonify

from schooloud.controller.OpenStackController import OpenStackController

openstack_controller = OpenStackController()


class ImageController:
    def __init__(self):
        pass

    def get_image_list(self, email):
        conn = openstack_controller.create_admin_connection()
        images = conn.list_images()
        image_list = []
        for image in images:
            image_list.append(
                {
                    "image_name": image.name,
                    "min_disk": image.min_disk,
                    "description": image.name
                }
            )

        return jsonify({"images": image_list})
