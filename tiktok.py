from TikTokApi import TikTokApi as tiktok #tiktokapi unofficial from github
import json

#api setup
verifyFp = "verify_lgbubcfd_dk7KGyI7_g0kv_4gJX_Bh2J_WLZIEvS6y6Cb"
api = tiktok.get_instance(costum_verifyFp=verifyFp, use_test_endpoints=True)
trending = api.by_hashtag('Belgium')


