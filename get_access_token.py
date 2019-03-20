from instagram_private_api import Client
import time

user_name = '#'
password = '#'

api = Client(user_name, password)

rank_token = Client.generate_uuid()

tags_to_search = ['crossfitcommunity', 'crossfitgirls', 'crossfitcoach', 'crossfitlife', 'crossfitwod',
                  'crossfitters', 'crossfitlovers','crossfitstrong', 'crossfitness', 'crossfitgym', 'crossfitfamily',
                  'crossfitopen', 'crossfitcouple', 'crossfitgirl', 'crossfitgames', 'crossfitopen2019', 'crossfitlove'
                  'crossfitbabes', 'crossfitstyle', 'crossfitchicks', 'crossfitmen', 'crossfitlifestyle', 'crossfitter',
                  'intheopen', 'intheopen2019','wods', 'wodoftheday', 'wodapalooza', 'wod', 'wodchallenge',
                  'crossfitwod', 'functionalfitness']


for tag in tags_to_search:
    count = 0
    print 'starting to search for', tag

    new_posts = api.feed_tag(tag, rank_token)['items']

    print new_posts[1]['id']

    for post in new_posts:
        post_id = post['id']
        try:
            api.post_like(post_id)
        except:
            print 'couldnt like a post'
        time.sleep(1)
        count +=1
    print count
