from data_vis.models import DataVisInteractive
from django.utils import timezone
import datetime


def create_posts():

    posts = DataVisInteractive.objects.filter(title_of_post='Title of 0')    

    if not posts:
        print("No posts.")

        for i in range(0,5):
            p = DataVisInteractive(
                    title_of_post = f"Title of data_vis int {i}",
                    date_of_post = timezone.now() - datetime.timedelta(days=i),
                    seo_description = "SEO",
                    publish = True,
                    intro_text = f'Intro text of data_vis int {i}',
                    concluding_text = f'Concluding text of data_vis int {i}',
                )        
            p.save()
        print("Made test data_vis int posts.")

        future_post = DataVisInteractive(
                    title_of_post = f"Title of Future Post data_vis int",
                    date_of_post = timezone.now() + datetime.timedelta(days=1000),
                    seo_description = "SEO",
                    publish = True,
                    intro_text = f'Intro text of data_vis int {i}',
                    concluding_text = f'Concluding text of data_vis int {i}',               
                    )
        
        future_post.save()
        print("Made future test data_vis int post.")

        not_published = DataVisInteractive(
            title_of_post = f"Title of Not Published data_vis int",
            date_of_post = timezone.now() - datetime.timedelta(days=1),
            seo_description = "SEO",
            publish = False,
            intro_text = f'Intro text of data_vis int {i}',
            concluding_text = f'Concluding text of data_vis int {i}',        
            )

        not_published.save()
        print("Made not published test data_vis int posts.")        

    else:
        print("Test posts present.")


def remove_all_posts():

    DataVisInteractive.objects.all().delete()
    print("Deleted all test data_vis int posts.")