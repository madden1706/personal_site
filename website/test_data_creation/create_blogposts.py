from blog.models import BlogPost
from django.utils import timezone
import datetime

def create_posts():

    blogposts = BlogPost.objects.filter(title_of_post='Title of 0')    

    if not blogposts:
        print("No posts.")

        for i in range(0,5):
            bp = BlogPost(
                    title_of_post = f"Title of {i}",
                    date_of_post = timezone.now() - datetime.timedelta(days=i),
                    blog_post = f"Text of {i}",
                    seo_description = "SEO",
                    publish = True,
                )        
            bp.save()
        print("Made test blogposts.")

        future_post = BlogPost(
                    title_of_post = f"Title of Future Post",
                    date_of_post = timezone.now() + datetime.timedelta(days=1000),
                    blog_post = f"Text of Future Post",
                    seo_description = "SEO",
                    publish = True,
                )
        
        future_post.save()
        print("Made future test blogpost.")

        not_published = BlogPost(
            title_of_post = f"Title of Not Published",
            date_of_post = timezone.now() - datetime.timedelta(days=1),
            blog_post = f"Text of Not Published",
            seo_description = "SEO",
            publish = False,
        )

        not_published.save()
        print("Made not published test blogpost.")        

    else:
        print("Test posts present.")


def remove_all_posts():

    BlogPost.objects.all().delete()
    print("Deleted all test blogposts.")






