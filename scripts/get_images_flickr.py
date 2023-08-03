import flickrapi
from config import FLICKR_API_KEY, FLICKR_API_SECRET, FLICKR_USER_ID

flickr = flickrapi.FlickrAPI(FLICKR_API_KEY, FLICKR_API_SECRET, format='parsed-json')

def get_photosets():
    sets = flickr.photosets.getList(user_id=FLICKR_USER_ID)
    photosets = sets['photosets']['photoset']
    for x in photosets:
        yield {x['title']['_content']:x['id']}
        
def get_urls(id_):
    photos = flickr.photosets.getPhotos(photoset_id=id_)['photoset']['photo']
    for photo in photos:
        photo_url = flickr.photos.getSizes(photo_id=photo['id'])['sizes']['size'][-1]['source']
        yield photo_url