import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "tPdTOW1w2nOqWCCZ39mzCmHH77XdTO6p1P6eFDlvTgkl"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields": [["checkout_price","base_price","discount percent","emailer_for_promotion","homepage_featured","op_area","discount_y/n","center_id_10","center_id_11","center_id_13","center_id_14","center_id_17","center_id_20","center_id_23","center_id_24","center_id_26","center_id_27","center_id_29","center_id_30","center_id_32","center_id_34","center_id_36","center_id_39","center_id_41","center_id_42","center_id_43","center_id_50","center_id_51","center_id_52","center_id_53","center_id_55","center_id_57","center_id_58","center_id_59","center_id_61","center_id_64","center_id_65","center_id_66","center_id_67","center_id_68","center_id_72","center_id_73","center_id_74","center_id_75","center_id_76","center_id_77","center_id_80","center_id_81","center_id_83","center_id_86","center_id_88","center_id_89","center_id_91","center_id_92","center_id_93","center_id_94","center_id_97","center_id_99","center_id_101","center_id_102","center_id_104","center_id_106","center_id_108","center_id_109","center_id_110","center_id_113","center_id_124","center_id_126","center_id_129","center_id_132","center_id_137","center_id_139","center_id_143","center_id_145","center_id_146","center_id_149","center_id_152","center_id_153","center_id_157","center_id_161","center_id_162","center_id_174","center_id_177","center_id_186","meal_id_1062","meal_id_1109","meal_id_1198","meal_id_1207","meal_id_1216","meal_id_1230","meal_id_1247","meal_id_1248","meal_id_1311","meal_id_1438","meal_id_1445","meal_id_1525","meal_id_1543","meal_id_1558","meal_id_1571","meal_id_1727","meal_id_1754","meal_id_1770","meal_id_1778","meal_id_1803","meal_id_1847","meal_id_1878","meal_id_1885","meal_id_1902","meal_id_1962","meal_id_1971","meal_id_1993","meal_id_2104","meal_id_2126","meal_id_2139","meal_id_2290","meal_id_2304","meal_id_2306","meal_id_2322","meal_id_2444","meal_id_2490","meal_id_2492","meal_id_2494","meal_id_2539","meal_id_2569","meal_id_2577","meal_id_2581","meal_id_2631","meal_id_2640","meal_id_2664","meal_id_2704","meal_id_2707","meal_id_2760","meal_id_2826","meal_id_2867","meal_id_2956","region_code_23","region_code_34","region_code_35","region_code_56","region_code_71","region_code_77","region_code_85","region_code_93","center_type_TYPE_A","center_type_TYPE_B","center_type_TYPE_C","category_Beverages","category_Biryani","category_Desert","category_Extras","category_Fish","category_Other_Snacks","category_Pasta","category_Pizza","category_Rice_Bowl","category_Salad","category_Sandwich","category_Seafood","category_Soup","category_Starters","cuisine_Continental","cuisine_Indian","cuisine_Italian","cuisine_Thai","city_enc_4_CH1","city_enc_4_CH2",  "city_enc_4_CH3","city_enc_4_CH4"]], "values": [[-0.907186,-0.999378,-0.497726,0,0,6.3,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/1ef1a65a-105a-4e3a-875c-f99c3a972504/predictions?version=2022-06-14', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
#print(response_scoring.json())
pred=response_scoring.json()
print(pred['predictions'][0]['values'][0][0])