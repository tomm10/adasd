""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy.util import smart_run



# login credentials
insta_username = 'meetingmyplanet'
insta_password = 't40B065s910.'

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)


with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                      delimit_by_numbers=True,
                                       max_followers=4590,
                                        min_followers=200,
                                        min_following=100)
    
    session.set_skip_users(skip_private=False,
                                    skip_no_profile_pic=False,
                                    skip_business=False)
    
    session.set_delimit_commenting(enabled=True, max=None, min=10)
    session.set_comments(['Awesome picture @{}',
                          'I just check your gallery and really loved it @{}',
                          'I like your stuff, its amazing @{}, check my profile',
                          'I really like your content, is awesome @{}',
                          'Wooow! amazing picture @{}, check my content',
                          'Your profile is amazing @{}, check mine',
                          'Nice pic, really like it @{}'])

    session.set_delimit_commenting(enabled=True, max=50, min=5)
    
    # activity
    session.follow_likers (['travelandleisure' , 'culture' , 'buzztraveller'],
                                   photos_grab_amount = 3,
                                   follow_likers_per_photo = 15,
                                   randomize=False,
                                   sleep_delay=0)

    session.unfollow_users(amount=50, nonFollowers=True, style="RANDOM",
                                   unfollow_after=42*60*60,
                                   sleep_delay=0)
    
    session.like_by_tags(["beautifuldestinations"], amount=9)
    session.like_by_tags(["instatravel"], amount=9)
    session.like_by_tags(["photooftheday"], amount=9)
    session.like_by_tags(["naturephotography"], amount=9)
    session.like_by_tags(["landscapephotography"], amount=9)
    session.like_by_tags(["tlpicks"], amount=9)



