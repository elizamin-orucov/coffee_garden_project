class Uploader:

    @staticmethod
    def product_image_uploader(instance, filename):
        return f"products/{instance.product.slug}/{filename}"

    @staticmethod
    def news_image_uploader(instance, filename):
        return f"news/{instance.news.slug}/{filename}"

    @staticmethod
    def event_image_uploader(instance, filename):
        return f"events/{instance.event.title}/{filename}"


