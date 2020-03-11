from finna_client import FinnaClient
import pandas as pd

IMAGE_BASE = 'https://api.finna.fi'

finna = FinnaClient()

def get_finna_content(image):
  
  result = finna.get_record(image, fields=['title', 'primaryAuthors', 'year', 'source', 'collections', 'imageRights', 'images'])
  
  entry = {}
  
  entry['signum'] = image
  entry['title'] = result['title']
  entry['author'] = result['primaryAuthors'][0]
  entry['year'] = result['year']
  entry['source'] = result['source'][0]['translated']
  entry['rights'] = result['imageRights']['copyright']
  entry['collection'] = ' / '.join(result['collections']) 
  entry['url'] = IMAGE_BASE + result['images'][0]
      
  return(entry)

wanted_images = ['musketti.M012:SUK35:44', 'musketti.M012:SUK35:36', 'musketti.M012:SUK35:133', 'musketti.M012:SUK35:64', 'musketti.M012:SUK35:67', 'musketti.M012:SUK35:55', 'musketti.M012:SUK35:84', 'musketti.M012:SUK35:8', 'musketti.M012:SUK35:9', 'musketti.M012:SUK35:52', 'musketti.M012:SUK36:358', 'musketti.M012:SUK36:66', 'musketti.M012:SUK36:67', 'musketti.M012:SUK36:70', 'musketti.M012:SUK36:308', 'musketti.M012:SUK36:350', 'musketti.M012:SUK36:63', 'musketti.M012:SUK36:65', 'musketti.M012:SUK36:68', 'musketti.M012:SUK36:69', 'musketti.M012:SUK36:129', 'musketti.M012:SUK36:171', 'musketti.M012:SUK36:64', 'musketti.M012:SUK36:256']

image_list = []

for image in wanted_images:
  
  finna_content = get_finna_content(image)
  print(image)
  print(finna_content)
  print('')
  
  if finna_content:
      image_list.append(finna_content)

if len(image_list) != 0:
  
  df = pd.DataFrame.from_dict(image_list)
  df.to_csv("data/finna_image_info.csv", index=False)

