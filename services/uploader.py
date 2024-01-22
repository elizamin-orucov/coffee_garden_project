class Uploader:

    @staticmethod
    def product_image_uploader(instance, filename):
        return f"products/{instance.product.name}/{filename}"

    @staticmethod
    def news_image_uploader(instance, filename):
        return f"news/{instance.news}/{filename}"


