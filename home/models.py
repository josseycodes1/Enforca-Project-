from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=255)  # Icon in SVG format or FontAwesome class

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='slider_images/')
    button_text = models.CharField(max_length=100, blank=True)
    button_url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"Contact Info: {self.phone}, {self.email}"


class Feature(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=255)  # Icon in SVG format or FontAwesome class

    def __str__(self):
        return self.name


class HomePage(models.Model):
    slider = models.ForeignKey(Slider, on_delete=models.CASCADE, related_name='home_page')
    services = models.ManyToManyField(Service, through='HomePageService')
    features = models.ManyToManyField(Feature, through='HomePageFeature')
    contact_info = models.OneToOneField(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return "HomePage Content"


# Intermediate Models for Many-to-Many Relationships
class HomePageService(models.Model):
    homepage = models.ForeignKey(HomePage, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)


class HomePageFeature(models.Model):
    homepage = models.ForeignKey(HomePage, on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
