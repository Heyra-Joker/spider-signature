# 抖音 dy douyin dou yin 最新 a_bogus ttwid X-Bogus 计算 更新时间 2023-08-31

我们都知道 抖音最新上了 a_bogus 算法，花了一点时间解决了 效果如下(Web) 版本:

测试中会发现```ttwid```,```a_bogus```,```user-agent```，```msToken```是必须的，但是到目前为止```X-Bogus```貌似某些接口还没有校验。

### a_bogus

最新版本的```a_bogus```无论是```GET```请求还是```POST```请求都是需要计算的，并且计算方式和```X-Bogus```大同小异，已经搞过```X-bogus```的朋友可以自行尝试一下，捞函数的部分还是比较困难的，```a_bogus```也是使用```jsvmp```。

### 测试地址如下

Base64 解码: aHR0cDovLzE4Mi40NC4xNy4xMTY6Njc4OS9keS1zaWduYXR1cmU=

每天8点更新100次测试, 想要测试账号的朋友可以联系QQ【base64】：NDQ3NTkyNzc0 备注:dy

请求案例:

```shell
curl --location --request POST 'aHR0cDovLzE4Mi40NC4xNy4xMTY6Njc4OS9keS1zaWduYXR1cmU=' \
--header 'Content-Type: application/json' \
--header 'Accept: */*' \
--data-raw '{
    "token": "bf207221-3879-4ea1-b390-ed4a6ff41004",
    "url": "https://www.douyin.com/aweme/v1/web/aweme/detail/?aweme_id=7052149213647342862&aid=1128&version_name=23.5.0&device_platform=android&os_version=2333",
    "data": {} # 如果是post请求可以添加data
}'
```

获取结果:

```json
{
    "code":0,
    "msg":"success",
    "data":{
        "note":"返回的user-agent必须使用，并且你的请求中保证 referer 与 authority 是正确的, 到目前为止 cookie 中的 ttwid 也是必须的，详情查看案例",
        "status":"ok",
        "data":{
            "url":"https://www.douyin.com/aweme/v1/web/aweme/detail/?aweme_id=7052149213647342862&amp;aid=1128&amp;version_name=23.5.0&amp;device_platform=android&amp;os_version=2333&amp;msToken=_9XcLxMOd8Mx__7bMEXwi5fSYtVVRsTI9T63VD9OWf7pINn3QdjGUuCFXpayIOAJh8VTh8naEwS6j1yVRva8sOmnwQypaB6RtEduypTSlAVthDnAim3AyZaPvi0gHqY%3D&amp;a_bogus=D7MdfOZVMsR1afV6B7kz9e4mZKS0YWRNgZEzEk-cVtLd&amp;X-Bogus=DFSzswSLewJANrmsty3ru09WcBng",
            "ua":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
          "ttwid": "1%7CeD9kdw_lEuins6r_gtH76HPPq4tkaibKQrp0LULZps8%7C1693464847%7Cd242543092d387e13eb636d5ba97b9ecbc601a230d93369464ddf538e786890f"
        },
        "token_count":"剩余Token次数为: 99"
    }
}
```

### 注意:

为确保一致性接下来的请求必须使用 ```ua``` 和返回的 ```ttwid```

```python
import requests

cookies = {
    'ttwid': '1%7CmpYTi1goGC0adR0cCiRXi9cuBb2H1bK_e5U7qbyAYtY%7C1693459855%7Ce6cc5f347a0c1b6570c113082168f74e58087649c30382de093663243af1abdd',
}

headers = {
    'authority': 'www.iesdouyin.com', # 这里必须和你的 host 一致
  	# 正常 referer 即可
    'referer': 'https://www.iesdouyin.com/share/video/7267887627636837673/?region=CN&mid=7236664966387271682&u_code=4aacl8fi0b0k&did=MS4wLjABAAAAFObUk9-cB96WUY51tzzxUB-rA-Znp1IUqgpe8KjP0a52EudcSS-8OKG6Y_ccfFD7&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=Lf7w_g03wFW8o.B8fqoyjZnnPoYUSI1Qkxl0mWyy3mo-&share_version=170400&ts=1693301622&from_ssr=1&from=web_code_link',
  	# 使用返回的ua确保一致性
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
}

url = "https://www.douyin.com/aweme/v1/web/aweme/detail/?aweme_id=7052149213647342862&aid=1128&version_name=23.5.0&device_platform=android&os_version=2333&msToken=_9XcLxMOd8Mx__7bMEXwi5fSYtVVRsTI9T63VD9OWf7pINn3QdjGUuCFXpayIOAJh8VTh8naEwS6j1yVRva8sOmnwQypaB6RtEduypTSlAVthDnAim3AyZaPvi0gHqY%3D&a_bogus=QJBYvcZVMsR1afV6-7kz9e4mZuD0YW4QgZEzEh-X8ULv&X-Bogus=DFSzswSLewJANrmsty3Nc09WcBr8"
response = requests.get(url, cookies=cookies, headers=headers)
print(response.text)
```

响应:

```json
{"aweme_detail": {"activity_video_type": -1, "admire_auth": {"admire_button": 0, "author_can_admire": 0, "exit_admire_in_aweme_post": 0, "is_admire": 0, "is_click_admire_icon_recently": 0, "is_fifty_admire_author_stable_fans": 0, "is_iron_fans_in_aweme_post": 0, "is_show_admire_button": 0, "is_show_admire_tab": 0}, "anchors": null, "authentication_token": "MS4wLjAAAAAA88XNKQPTK38huEOW8f-1ud4uILH3RYKEF00UfGrY-kM7oNVZSk-8ZqXiX512lSWht-_DwzPEzwog3QmD4-vPbNMfOaWuPUVyZbBMxuCgVUXsJVyYgT39B4Atk8HqUSS6-H_lisBUiQEIGMloP9YMWBOLHSe3X_F9H6MhdP1APlUQJWE4Ypi5d8zfluK2bM4TBy5WpXUh-JNC6WStQS7YjM6bpIJVTEZXSMhMaO02uxw", "author": {"avatar_thumb": {"height": 720, "uri": "100x100/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a", "url_list": ["https://p6.douyinpic.com/aweme/100x100/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.webp?from=116350172", "https://p26.douyinpic.com/aweme/100x100/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.webp?from=116350172", "https://p11.douyinpic.com/aweme/100x100/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.webp?from=116350172", "https://p6.douyinpic.com/aweme/100x100/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.jpeg?from=116350172"], "width": 720}, "cf_list": null, "close_friend_type": 0, "contacts_status": 2, "contrail_list": null, "cover_url": [{"height": 720, "uri": "c8510002be9a3a61aad2", "url_list": ["https://p5-a-sign.douyinpic.com/obj/c8510002be9a3a61aad2?x-expires=1694671200&x-signature=OmDL%2F3lMPRd%2BWXrIvb2HEAb4msQ%3D&from=116350172", "https://p3-sign.douyinpic.com/obj/c8510002be9a3a61aad2?x-expires=1694671200&x-signature=0bXmwLg91KKnbmTHgf9hn89q91Q%3D&from=116350172", "https://p96-sign.douyinpic.com/obj/c8510002be9a3a61aad2?x-expires=1694671200&x-signature=bmp3SfBalkjualOhyCY5fu0%2FPYU%3D&from=116350172"], "width": 720}], "create_time": 0, "custom_verify": "", "data_label_list": null, "endorsement_info_list": null, "enterprise_verify_reason": "", "familiar_visitor_user": null, "favoriting_count": 1072, "follow_status": 0, "follow_status_err_code": 1, "follower_count": 0, "follower_list_secondary_information_struct": null, "follower_status": 0, "following_count": 0, "im_role_ids": null, "is_ad_fake": false, "is_ban": false, "is_blocked_v2": false, "is_blocking_v2": false, "is_cf": 0, "live_high_value": 0, "max_follower_count": 0, "nickname": "设计师阿爽", "not_seen_item_id_list": null, "not_seen_item_id_list_v2": null, "offline_info_list": null, "personal_tag_list": null, "prevent_download": false, "risk_notice_text": "", "sec_uid": "MS4wLjABAAAAAUNPjSuAGItEmEFdrQ7_jyUakTH956APYHzMaZNE9ok", "secret": 0, "share_info": {"share_desc": "", "share_desc_info": "", "share_qrcode_url": {"height": 720, "uri": "6f93001a279d8aade8c9", "url_list": ["https://p96-sign.douyinpic.com/obj/6f93001a279d8aade8c9?x-expires=1693483200&x-signature=aO0w0KyQZRdUHIt447P0foHdpCE%3D&from=116350172", "https://p11-sign.douyinpic.com/obj/6f93001a279d8aade8c9?x-expires=1693483200&x-signature=QyRbZJeOsMHieEF1nitv0qJxJgg%3D&from=116350172", "https://p5-sign.douyinpic.com/obj/6f93001a279d8aade8c9?x-expires=1693483200&x-signature=yd8PfYXNKCiMnT%2FUfTDC7I%2FMqPw%3D&from=116350172"], "width": 720}, "share_title": "", "share_title_myself": "", "share_title_other": "", "share_url": "", "share_weibo_desc": ""}, "short_id": "612877836", "signature": "家居一姐，买家居家电就找阿爽\n商务合作+V：XJW33446688\n全屋设计+V：po7465\n邀请阿爽去你家串门做客+V：ashuangtj\n售后投诉+V：ashuang520-\n日常好物 @设计师阿爽生活号", "signature_extra": null, "special_follow_status": 0, "special_people_labels": null, "status": 1, "text_extra": null, "total_favorited": 127276097, "uid": "56612823293", "unique_id": "spzp_04", "user_age": 35, "user_canceled": false, "user_permissions": null, "verification_type": 1}, "author_mask_tag": 0, "author_user_id": 56612823293, "aweme_control": {"can_comment": true, "can_forward": true, "can_share": true, "can_show_comment": true}, "aweme_id": "7052149213647342862", "aweme_type": 0, "book_bar": {}, "boost_status": 0, "challenge_position": null, "chapter_list": null, "collect_stat": 0, "collection_corner_mark": 0, "comment_gid": 7052149213647342862, "comment_list": null, "comment_permission_info": {"can_comment": true, "comment_permission_status": 0, "item_detail_entry": true, "press_entry": true, "toast_guide": false}, "comment_words_recommend": {"zero_comment": null}, "commerce_config_data": null, "common_bar_info": "[]", "component_info_v2": "{\"desc_lines_limit\":0,\"hide_marquee\":false}", "cover_labels": null, "create_scale_type": null, "create_time": 1641956467, "desc": "20万人喜欢的玄关，每个细节做到极致！赶紧来抄作业~#玄关 #装修 ", "descendants": {"notify_msg": "头条", "platforms": ["toutiao"]}, "digg_lottie": {"can_bomb": 0, "lottie_id": ""}, "disable_relation_bar": 0, "dislike_dimension_list": null, "dislike_dimension_list_v2": null, "distribute_circle": {"campus_block_interaction": false, "distribute_type": 0, "is_campus": false}, "duet_aggregate_in_music_tab": false, "duration": 48951, "feed_comment_config": {"input_config_text": "善语结善缘，恶言伤人心"}, "geofencing": [], "geofencing_regions": null, "group_id": "7052149213647342862", "guide_scene_info": {"diamond_expose_info_str": "", "feed_origin_gid_info_str": "", "guide_scene_type": 0}, "hybrid_label": null, "image_album_music_info": {"begin_time": -1, "end_time": -1, "volume": -1}, "image_comment": {}, "image_crop_ctrl": 0, "image_infos": null, "image_list": null, "images": null, "img_bitrate": null, "impression_data": {"group_id_list_a": [], "group_id_list_b": [], "group_id_list_c": [], "similar_id_list_a": null, "similar_id_list_b": null}, "interaction_stickers": null, "is_ads": false, "is_collects_selected": 0, "is_duet_sing": false, "is_image_beat": false, "is_life_item": false, "is_share_post": false, "is_story": 0, "is_top": 0, "item_warn_notification": {"content": "", "show": false, "type": 0}, "jump_tab_info_list": null, "label_top_text": null, "live_appointment_info": {}, "long_video": null, "media_type": 4, "music": {"album": "", "artist_user_infos": null, "artists": [], "audition_duration": 48, "author": "设计师阿爽", "author_deleted": false, "author_position": null, "author_status": 1, "avatar_large": {"height": 720, "uri": "1080x1080/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a", "url_list": ["https://p6.douyinpic.com/aweme/1080x1080/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.webp?from=116350172", "https://p26.douyinpic.com/aweme/1080x1080/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.webp?from=116350172", "https://p11.douyinpic.com/aweme/1080x1080/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.webp?from=116350172", "https://p6.douyinpic.com/aweme/1080x1080/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.jpeg?from=116350172"], "width": 720}, "avatar_medium": {"height": 720, "uri": "720x720/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a", "url_list": ["https://p26.douyinpic.com/aweme/720x720/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.webp?from=116350172", "https://p11.douyinpic.com/aweme/720x720/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.webp?from=116350172", "https://p3.douyinpic.com/aweme/720x720/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.webp?from=116350172", "https://p26.douyinpic.com/aweme/720x720/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.jpeg?from=116350172"], "width": 720}, "avatar_thumb": {"height": 720, "uri": "100x100/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a", "url_list": ["https://p11.douyinpic.com/aweme/100x100/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.webp?from=116350172", "https://p6.douyinpic.com/aweme/100x100/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.webp?from=116350172", "https://p26.douyinpic.com/aweme/100x100/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.webp?from=116350172", "https://p11.douyinpic.com/aweme/100x100/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.jpeg?from=116350172"], "width": 720}, "binded_challenge_id": 0, "can_background_play": true, "collect_stat": 0, "cover_hd": {"height": 720, "uri": "1080x1080/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a", "url_list": ["https://p6.douyinpic.com/aweme/1080x1080/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.webp?from=116350172", "https://p26.douyinpic.com/aweme/1080x1080/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.webp?from=116350172", "https://p11.douyinpic.com/aweme/1080x1080/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.webp?from=116350172", "https://p6.douyinpic.com/aweme/1080x1080/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.jpeg?from=116350172"], "width": 720}, "cover_large": {"height": 720, "uri": "1080x1080/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a", "url_list": ["https://p6.douyinpic.com/aweme/1080x1080/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.webp?from=116350172", "https://p26.douyinpic.com/aweme/1080x1080/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.webp?from=116350172", "https://p11.douyinpic.com/aweme/1080x1080/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.webp?from=116350172", "https://p6.douyinpic.com/aweme/1080x1080/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.jpeg?from=116350172"], "width": 720}, "cover_medium": {"height": 720, "uri": "720x720/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a", "url_list": ["https://p26.douyinpic.com/aweme/720x720/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.webp?from=116350172", "https://p11.douyinpic.com/aweme/720x720/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.webp?from=116350172", "https://p3.douyinpic.com/aweme/720x720/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.webp?from=116350172", "https://p26.douyinpic.com/aweme/720x720/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.jpeg?from=116350172"], "width": 720}, "cover_thumb": {"height": 720, "uri": "100x100/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a", "url_list": ["https://p11.douyinpic.com/aweme/100x100/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.webp?from=116350172", "https://p6.douyinpic.com/aweme/100x100/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.webp?from=116350172", "https://p26.douyinpic.com/aweme/100x100/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.webp?from=116350172", "https://p11.douyinpic.com/aweme/100x100/aweme-avatar/mosaic-legacy_2cf2600018fbdf006db1a.jpeg?from=116350172"], "width": 720}, "dmv_auto_show": false, "dsp_status": 10, "duration": 48, "end_time": 0, "external_song_info": [], "extra": "{\"cover_colors\":null,\"music_tagging\":{\"Languages\":null,\"Moods\":null,\"Genres\":null,\"Themes\":null,\"AEDs\":null,\"SingingVersions\":null,\"Instruments\":null},\"is_red\":0,\"music_label_id\":null,\"extract_item_id\":7052149213647342862,\"is_aed_music\":0,\"review_unshelve_reason\":0,\"beats\":{\"merged_beats\":\"https://sf6-cdn-tos.douyinstatic.com/obj/ies-music/strong_beat/v3/1721722928044045\",\"audio_effect_onset\":\"https://sf6-cdn-tos.douyinstatic.com/obj/ies-music/strong_beat/v3/1721722925756424\",\"beats_tracker\":\"https://sf86-cdn-tos.douyinstatic.com/obj/ies-music/strong_beat/v3/1721722927968270\",\"energy_trace\":\"https://sf6-cdn-tos.douyinstatic.com/obj/ies-music/strong_beat/v3/1721722925712398\"},\"douyin_beats_info\":{},\"schedule_search_time\":0,\"with_aed_model\":1,\"dsp_switch\":0,\"reviewed\":1,\"hotsoon_review_time\":-1,\"aggregate_exempt_conf\":[],\"is_subsidy_exp\":false,\"has_edited\":0,\"image_beats_url\":\"https://sf86-cdn-tos.douyinstatic.com/obj/ies-music/strong_beat/v3/1721722927968270\"}", "id": 7052149360633236231, "id_str": "7052149360633236231", "is_audio_url_with_cookie": false, "is_commerce_music": false, "is_del_video": false, "is_matched_metadata": false, "is_original": false, "is_original_sound": true, "is_pgc": false, "is_restricted": false, "is_video_self_see": false, "luna_info": {"is_luna_user": false}, "lyric_short_position": null, "mid": "7052149360633236231", "music_chart_ranks": null, "music_collect_count": 0, "music_cover_atmosphere_color_value": "", "music_image_beats": {"music_image_beats_url": {"height": 720, "uri": "ies-music/strong_beat/v3/1721722927968270", "url_list": ["https://sf86-cdn-tos.douyinstatic.com/obj/ies-music/strong_beat/v3/1721722927968270"], "width": 720}}, "music_status": 1, "musician_user_infos": null, "mute_share": false, "offline_desc": "", "owner_handle": "spzp_04", "owner_id": "56612823293", "owner_nickname": "设计师阿爽", "pgc_music_type": 2, "play_url": {"height": 720, "uri": "https://sf3-cdn-tos.douyinstatic.com/obj/ies-music/7052149359034600228.mp3", "url_key": "7052149360633236231", "url_list": ["https://sf3-cdn-tos.douyinstatic.com/obj/ies-music/7052149359034600228.mp3", "https://sf86-cdn-tos.douyinstatic.com/obj/ies-music/7052149359034600228.mp3"], "width": 720}, "position": null, "prevent_download": false, "prevent_item_download_status": 0, "preview_end_time": 0, "preview_start_time": 0, "reason_type": 0, "redirect": false, "schema_url": "", "search_impr": {"entity_id": "7052149360633236231"}, "sec_uid": "MS4wLjABAAAAAUNPjSuAGItEmEFdrQ7_jyUakTH956APYHzMaZNE9ok", "shoot_duration": 48, "source_platform": 23, "start_time": 0, "status": 1, "strong_beat_url": {"height": 720, "uri": "https://sf3-cdn-tos.douyinstatic.com/obj/ies-music/pattern/bac974e9ca56c5362f8c58c9088502b2.json", "url_list": ["https://sf3-cdn-tos.douyinstatic.com/obj/ies-music/pattern/bac974e9ca56c5362f8c58c9088502b2.json", "https://sf86-cdn-tos.douyinstatic.com/obj/ies-music/pattern/bac974e9ca56c5362f8c58c9088502b2.json"], "width": 720}, "tag_list": null, "title": "@设计师阿爽创作的原声", "unshelve_countries": null, "user_count": 0, "video_duration": 48}, "nickname_position": null, "origin_comment_ids": null, "origin_text_extra": [], "original_images": null, "packed_clips": null, "photo_search_entrance": {"ecom_type": 0}, "position": null, "press_panel_info": "[{\"interactive\":[\"2_story\",\"2_friend\"]},{\"feedback\":[\"rr_feedback\",\"dislike\",\"ignore\",\"block\",\"unfollow\",\"sever\",\"dislike_collect\"]},{\"control\":[\"speed\",\"auth\",\"delete\",\"save\",\"collect\",\"reward\",\"bg_play\",\"duet\",\"together\"]}]", "preview_title": "20万人喜欢的玄关，每个细节做到极致！赶紧来抄作业~#玄关 #装修 ", "preview_video_status": 1, "promotions": [], "rate": 12, "ref_tts_id_list": null, "ref_voice_modify_id_list": null, "region": "", "relation_labels": null, "reply_smart_emojis": null, "search_impr": {"entity_id": "7052149213647342862", "entity_type": "GENERAL"}, "series_paid_info": {"item_price": 0, "series_paid_status": 0}, "share_info": {"share_desc": "在抖音，记录美好生活", "share_desc_info": "#在抖音，记录美好生活#20万人喜欢的玄关，每个细节做到极致！赶紧来抄作业~#玄关 #装修 ", "share_link_desc": "9.43 HIV:/ 复制打开抖音，看看【设计师阿爽的作品】20万人喜欢的玄关，每个细节做到极致！赶紧来抄作业... %s", "share_url": "https://www.iesdouyin.com/share/video/7052149213647342862/?region=CN&mid=7052149360633236231&u_code=-1&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=hBMolUu_aMaL11UGmzb8WeGgRGVxpMnoT0I89qhRi.g-&share_version=230500&ts=1693465014&from_ssr=1"}, "share_url": "https://www.iesdouyin.com/share/video/7052149213647342862/?region=CN&mid=7052149360633236231&u_code=-1&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=hBMolUu_aMaL11UGmzb8WeGgRGVxpMnoT0I89qhRi.g-&share_version=230500&ts=1693465014&from_ssr=1", "should_open_ad_report": false, "show_follow_button": {}, "slides_music_beats": null, "social_tag_list": null, "standard_bar_info_list": null, "statistics": {"admire_count": 0, "aweme_id": "7052149213647342862", "collect_count": 38763, "comment_count": 2804, "digg_count": 132451, "play_count": 0, "share_count": 32411}, "status": {"allow_share": true, "aweme_id": "7052149213647342862", "in_reviewing": false, "is_delete": false, "is_prohibited": false, "listen_video_status": 2, "part_see": 0, "private_status": 0, "review_result": {"review_status": 0}}, "suggest_words": {"suggest_words": [{"extra_info": "{}", "hint_text": "气泡框词", "icon_url": "", "scene": "search_icon_rec", "words": [{"info": "{\"qrec_for_search\":\"{}\"}", "word": "玄关", "word_id": "6595527519481386254"}]}]}, "super_like_status": 0, "text_extra": [{"end": 29, "hashtag_id": "1615850559096836", "hashtag_name": "玄关", "is_commerce": false, "start": 26, "type": 1}, {"end": 33, "hashtag_id": "1573830358902798", "hashtag_name": "装修", "is_commerce": false, "start": 30, "type": 1}], "tts_id_list": null, "uniqid_position": null, "user_digged": 0, "user_recommend_status": 0, "video": {"big_thumbs": null, "bit_rate": [{"FPS": 29, "HDR_bit": "", "HDR_type": "", "bit_rate": 586978, "gear_name": "adapt_lowest_720_1", "is_bytevc1": 1, "is_h265": 1, "play_addr": {"data_size": 3591648, "file_cs": "c:0-41561-1aa7|d:0-1795823-7844,1795824-3591647-693e|a:v0200fg10000c7f3h9bc77u8000rsiog", "file_hash": "2a1f18b921d454e5e67be929cc17ee71", "height": 1280, "uri": "v0200fg10000c7f3h9bc77u8000rsiog", "url_key": "v0200fg10000c7f3h9bc77u8000rsiog_bytevc1_720p_586978", "url_list": ["https://v99-coldx.douyinvod.com/4aa547a506ab11629d53ebc2701aebb1/64f047f6/video/tos/cn/tos-cn-ve-15-alinc2/cab12f0e1e3a4aa7b72919ac1dd5aef2/?a=1128&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=573&bt=573&cs=2&ds=3&ft=GNvhKpVVywSWRso80mo~ySqTeaApxVxV6vrK983lSto0g3&mime_type=video_mp4&qs=15&rc=aDhlOmQ8NTY0ODY8ZjszZEBpamx1Mzs6Zjw2OjMzNGkzM0AyLTRfYzY2NWAxX2EtNDMvYSNscC0tcjRfZWNgLS1kLS9zcw%3D%3D&btag=e000a0000&dy_q=1693465014&l=202308311456549CFCC3448902F10F01AF", "https://v11-cold1.douyinvod.com/ec289d08053eed15017346b947768fb8/64f047f6/video/tos/cn/tos-cn-ve-15-alinc2/cab12f0e1e3a4aa7b72919ac1dd5aef2/?a=1128&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=573&bt=573&cs=2&ds=3&ft=GNvhKpVVywSWRso80mo~ySqTeaApxVxV6vrK983lSto0g3&mime_type=video_mp4&qs=15&rc=aDhlOmQ8NTY0ODY8ZjszZEBpamx1Mzs6Zjw2OjMzNGkzM0AyLTRfYzY2NWAxX2EtNDMvYSNscC0tcjRfZWNgLS1kLS9zcw%3D%3D&btag=e000a0000&dy_q=1693465014&l=202308311456549CFCC3448902F10F01AF", "https://api-play.amemv.com/aweme/v1/play/?video_id=v0200fg10000c7f3h9bc77u8000rsiog&line=0&file_id=2a60780cd9b345c1839299fab77b055e&sign=2a1f18b921d454e5e67be929cc17ee71&is_play_url=1&source=PackSourceEnum_AWEME_DETAIL", "https://api.amemv.com/aweme/v1/play/?video_id=v0200fg10000c7f3h9bc77u8000rsiog&line=1&file_id=2a60780cd9b345c1839299fab77b055e&sign=2a1f18b921d454e5e67be929cc17ee71&is_play_url=1&source=PackSourceEnum_AWEME_DETAIL"], "width": 720}, "quality_type": 15, "video_extra": "{\"PktOffsetMap\":\"\"}"}, {"FPS": 29, "HDR_bit": "", "HDR_type": "", "bit_rate": 473206, "gear_name": "adapt_540_1", "is_bytevc1": 1, "is_h265": 1, "play_addr": {"data_size": 2895492, "file_cs": "c:0-41561-11ab|d:0-1447745-15c1,1447746-2895491-8c42|a:v0200fg10000c7f3h9bc77u8000rsiog", "file_hash": "c06ca8dfb8d6b00d56be2f1c6bd019f0", "height": 1024, "uri": "v0200fg10000c7f3h9bc77u8000rsiog", "url_key": "v0200fg10000c7f3h9bc77u8000rsiog_bytevc1_540p_473206", "url_list": ["https://v11-coldf.douyinvod.com/f3e623a2956cea90f1c156652786cb61/64f047f6/video/tos/cn/tos-cn-ve-15-alinc2/f2259bcaa0e345b4a2444907ff022ca3/?a=1128&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=462&bt=462&cs=2&ds=6&ft=GNvhKpVVywSWRso80mo~ySqTeaApxVxV6vrK983lSto0g3&mime_type=video_mp4&qs=11&rc=aTU3ZGU5PDU6OTQ7NjlmM0Bpamx1Mzs6Zjw2OjMzNGkzM0BfLl4yM2JeNi8xMjVfLTY2YSNscC0tcjRfZWNgLS1kLS9zcw%3D%3D&btag=e000a0000&dy_q=1693465014&l=202308311456549CFCC3448902F10F01AF", "https://v99-coldx.douyinvod.com/74848bfac5bc2f8256d40f80313d6390/64f047f6/video/tos/cn/tos-cn-ve-15-alinc2/f2259bcaa0e345b4a2444907ff022ca3/?a=1128&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=462&bt=462&cs=2&ds=6&ft=GNvhKpVVywSWRso80mo~ySqTeaApxVxV6vrK983lSto0g3&mime_type=video_mp4&qs=11&rc=aTU3ZGU5PDU6OTQ7NjlmM0Bpamx1Mzs6Zjw2OjMzNGkzM0BfLl4yM2JeNi8xMjVfLTY2YSNscC0tcjRfZWNgLS1kLS9zcw%3D%3D&btag=e000a0000&dy_q=1693465014&l=202308311456549CFCC3448902F10F01AF", "https://api-play.amemv.com/aweme/v1/play/?video_id=v0200fg10000c7f3h9bc77u8000rsiog&line=0&file_id=909c06b38851462792a9e66b5aa412bf&sign=c06ca8dfb8d6b00d56be2f1c6bd019f0&is_play_url=1&source=PackSourceEnum_AWEME_DETAIL", "https://api.amemv.com/aweme/v1/play/?video_id=v0200fg10000c7f3h9bc77u8000rsiog&line=1&file_id=909c06b38851462792a9e66b5aa412bf&sign=c06ca8dfb8d6b00d56be2f1c6bd019f0&is_play_url=1&source=PackSourceEnum_AWEME_DETAIL"], "width": 576}, "quality_type": 28, "video_extra": "{\"PktOffsetMap\":\"\"}"}], "bit_rate_audio": null, "cover": {"height": 1920, "uri": "tos-cn-i-dy/21eb039e0c0e46a3aad347b64cf9dcb3", "url_list": ["https://p6-sign.douyinpic.com/tos-cn-i-dy/21eb039e0c0e46a3aad347b64cf9dcb3~c5_300x400.webp?x-expires=1694671200&x-signature=8%2Ftc%2FsDwUplxfBQo1jNEvXzeqTA%3D&from=3213915784_large&s=PackSourceEnum_AWEME_DETAIL&se=false&sc=cover&biz_tag=aweme_video&l=202308311456549CFCC3448902F10F01AF", "https://p3-sign.douyinpic.com/tos-cn-i-dy/21eb039e0c0e46a3aad347b64cf9dcb3~c5_300x400.webp?x-expires=1694671200&x-signature=8WeRTgdHTWZM4sEGITFmstSU6RI%3D&from=3213915784_large&s=PackSourceEnum_AWEME_DETAIL&se=false&sc=cover&biz_tag=aweme_video&l=202308311456549CFCC3448902F10F01AF", "https://p11-sign.douyinpic.com/tos-cn-i-dy/21eb039e0c0e46a3aad347b64cf9dcb3~c5_300x400.webp?x-expires=1694671200&x-signature=zy%2Ft5hr1pCj2Pc7QOnHQ%2FNMorhc%3D&from=3213915784_large&s=PackSourceEnum_AWEME_DETAIL&se=false&sc=cover&biz_tag=aweme_video&l=202308311456549CFCC3448902F10F01AF", "https://p6-sign.douyinpic.com/tos-cn-i-dy/21eb039e0c0e46a3aad347b64cf9dcb3~c5_300x400.jpeg?x-expires=1694671200&x-signature=DVbhdybok4fTDrnFCvNqRYdRcyI%3D&from=3213915784_large&s=PackSourceEnum_AWEME_DETAIL&se=false&sc=cover&biz_tag=aweme_video&l=202308311456549CFCC3448902F10F01AF"], "width": 1080}, "cover_original_scale": {"height": 720, "uri": "tos-cn-i-dy/21eb039e0c0e46a3aad347b64cf9dcb3", "url_list": ["https://p6-sign.douyinpic.com/tos-cn-i-dy/21eb039e0c0e46a3aad347b64cf9dcb3~tplv-dy-360p.webp?x-expires=1694671200&x-signature=MbC8aFUQPCc3cWIPqE9RTbGeIbk%3D&from=3213915784&s=PackSourceEnum_AWEME_DETAIL&se=false&sc=origin_cover&biz_tag=aweme_video&l=202308311456549CFCC3448902F10F01AF", "https://p3-sign.douyinpic.com/tos-cn-i-dy/21eb039e0c0e46a3aad347b64cf9dcb3~tplv-dy-360p.webp?x-expires=1694671200&x-signature=RyxYuDsxfh1X8wx%2BHVxAtGEZFxo%3D&from=3213915784&s=PackSourceEnum_AWEME_DETAIL&se=false&sc=origin_cover&biz_tag=aweme_video&l=202308311456549CFCC3448902F10F01AF", "https://p11-sign.douyinpic.com/tos-cn-i-dy/21eb039e0c0e46a3aad347b64cf9dcb3~tplv-dy-360p.webp?x-expires=1694671200&x-signature=rvuM6CKK1G%2F1%2B5gy8llqRyem8jc%3D&from=3213915784&s=PackSourceEnum_AWEME_DETAIL&se=false&sc=origin_cover&biz_tag=aweme_video&l=202308311456549CFCC3448902F10F01AF", "https://p6-sign.douyinpic.com/tos-cn-i-dy/21eb039e0c0e46a3aad347b64cf9dcb3~tplv-dy-360p.jpeg?x-expires=1694671200&x-signature=WT1CFRDKTHZcaxxlAhZGkReKa2w%3D&from=3213915784&s=PackSourceEnum_AWEME_DETAIL&se=false&sc=origin_cover&biz_tag=aweme_video&l=202308311456549CFCC3448902F10F01AF"], "width": 720}, "duration": 48951, "dynamic_cover": {"height": 720, "uri": "tos-cn-i-dy/21eb039e0c0e46a3aad347b64cf9dcb3", "url_list": ["https://p6-sign.douyinpic.com/obj/tos-cn-i-dy/21eb039e0c0e46a3aad347b64cf9dcb3?x-expires=1694671200&x-signature=B%2BejNO4CgWD%2F3byVePAr0a3hvbg%3D&from=3213915784_large&s=PackSourceEnum_AWEME_DETAIL&se=false&sc=dynamic_cover&biz_tag=aweme_video&l=202308311456549CFCC3448902F10F01AF", "https://p3-sign.douyinpic.com/obj/tos-cn-i-dy/21eb039e0c0e46a3aad347b64cf9dcb3?x-expires=1694671200&x-signature=TtDBn6tEpiJb3AKglZmYS5oNVYk%3D&from=3213915784_large&s=PackSourceEnum_AWEME_DETAIL&se=false&sc=dynamic_cover&biz_tag=aweme_video&l=202308311456549CFCC3448902F10F01AF", "https://p11-sign.douyinpic.com/obj/tos-cn-i-dy/21eb039e0c0e46a3aad347b64cf9dcb3?x-expires=1694671200&x-signature=B%2Bidv0fy0RZ8N2g31FaobPXhdyg%3D&from=3213915784_large&s=PackSourceEnum_AWEME_DETAIL&se=false&sc=dynamic_cover&biz_tag=aweme_video&l=202308311456549CFCC3448902F10F01AF"], "width": 720}, "height": 1920, "is_h265": 0, "is_source_HDR": 0, "meta": "{\"loudness\":\"-12.7\",\"peak\":\"1\",\"qprf\":\"0.6206467747688293\",\"sr_score\":\"0.000\"}", "optimized_cover": {"height": 720, "uri": "tos-cn-i-dy/002ea2f1e66143ee9a87442c83bd8d09", "url_list": ["https://p26-sign.douyinpic.com/tos-cn-i-dy/002ea2f1e66143ee9a87442c83bd8d09~noop.webp?x-expires=1694671200&x-signature=lf%2FybLMA8lnMV2ExjvqctB9wJnY%3D&from=3213915784&s=PackSourceEnum_AWEME_DETAIL&se=false&sc=optimized_cover&biz_tag=aweme_video&l=202308311456549CFCC3448902F10F01AF", "https://p96-sign.douyinpic.com/tos-cn-i-dy/002ea2f1e66143ee9a87442c83bd8d09~noop.webp?x-expires=1694671200&x-signature=u1Y4%2F4gAaV1axMFDhoRHI1CYB5Y%3D&from=3213915784&s=PackSourceEnum_AWEME_DETAIL&se=false&sc=optimized_cover&biz_tag=aweme_video&l=202308311456549CFCC3448902F10F01AF", "https://p6-sign.douyinpic.com/tos-cn-i-dy/002ea2f1e66143ee9a87442c83bd8d09~noop.webp?x-expires=1694671200&x-signature=7myGCKUXlUm5v7cbSYmZxN%2BnQcs%3D&from=3213915784&s=PackSourceEnum_AWEME_DETAIL&se=false&sc=optimized_cover&biz_tag=aweme_video&l=202308311456549CFCC3448902F10F01AF", "https://p26-sign.douyinpic.com/tos-cn-i-dy/002ea2f1e66143ee9a87442c83bd8d09~noop.jpeg?x-expires=1694671200&x-signature=2O1Qsf1%2Bv7RlCHOJCXd4rRyJAmM%3D&from=3213915784&s=PackSourceEnum_AWEME_DETAIL&se=false&sc=optimized_cover&biz_tag=aweme_video&l=202308311456549CFCC3448902F10F01AF"], "width": 720}, "origin_cover": {"height": 720, "uri": "tos-cn-p-0015/c3c61fa64138491f8d5438a0b1296408_1641956472", "url_list": ["https://p26-sign.douyinpic.com/tos-cn-p-0015/c3c61fa64138491f8d5438a0b1296408_1641956472~tplv-dy-360p.webp?x-expires=1694671200&x-signature=qqptrfZ5AHAgiF1NLGTVfvLLbxI%3D&from=3213915784&s=PackSourceEnum_AWEME_DETAIL&se=false&sc=origin_cover&biz_tag=aweme_video&l=202308311456549CFCC3448902F10F01AF", "https://p11-sign.douyinpic.com/tos-cn-p-0015/c3c61fa64138491f8d5438a0b1296408_1641956472~tplv-dy-360p.webp?x-expires=1694671200&x-signature=RXgaYPtEflO%2FMUxXNMNy0RvkLy4%3D&from=3213915784&s=PackSourceEnum_AWEME_DETAIL&se=false&sc=origin_cover&biz_tag=aweme_video&l=202308311456549CFCC3448902F10F01AF", "https://p9-sign.douyinpic.com/tos-cn-p-0015/c3c61fa64138491f8d5438a0b1296408_1641956472~tplv-dy-360p.webp?x-expires=1694671200&x-signature=LFMAf%2FrlR4GJmqllt%2BvZkpYG0dA%3D&from=3213915784&s=PackSourceEnum_AWEME_DETAIL&se=false&sc=origin_cover&biz_tag=aweme_video&l=202308311456549CFCC3448902F10F01AF", "https://p26-sign.douyinpic.com/tos-cn-p-0015/c3c61fa64138491f8d5438a0b1296408_1641956472~tplv-dy-360p.jpeg?x-expires=1694671200&x-signature=Ec2fMEkVv%2BTWkjSA7Xq6Kq5zlDo%3D&from=3213915784&s=PackSourceEnum_AWEME_DETAIL&se=false&sc=origin_cover&biz_tag=aweme_video&l=202308311456549CFCC3448902F10F01AF"], "width": 720}, "play_addr": {"data_size": 9104818, "file_cs": "c:0-53722-c2e0|d:0-4552408-a641,4552409-9104817-6638|a:v0200fg10000c7f3h9bc77u8000rsiog", "file_hash": "e31fba27444fe97a8c2b4d9007eea78f", "height": 1024, "uri": "v0200fg10000c7f3h9bc77u8000rsiog", "url_key": "v0200fg10000c7f3h9bc77u8000rsiog_h264_540p_1491492", "url_list": ["https://v9-cold1.douyinvod.com/646073a0cbbe1c2144061100a718d022/64f047f6/video/tos/cn/tos-cn-ve-15-alinc2/1e047e56b0d14d7395ea49ddb547e134/?a=1128&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1456&bt=1456&cs=0&ds=6&ft=GNvhKpVVywSWRso80mo~ySqTeaApxVxV6vrK983lSto0g3&mime_type=video_mp4&qs=0&rc=OGVoNGc7ZmVkNDlpOTwzNUBpamx1Mzs6Zjw2OjMzNGkzM0BhMzY0L15fXzYxNjZeXzZfYSNscC0tcjRfZWNgLS1kLS9zcw%3D%3D&btag=e000a0000&dy_q=1693465014&l=202308311456549CFCC3448902F10F01AF", "https://v11-cold.douyinvod.com/e9b5cbfa8961978c8b290fc39b736d33/64f047f6/video/tos/cn/tos-cn-ve-15-alinc2/1e047e56b0d14d7395ea49ddb547e134/?a=1128&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1456&bt=1456&cs=0&ds=6&ft=GNvhKpVVywSWRso80mo~ySqTeaApxVxV6vrK983lSto0g3&mime_type=video_mp4&qs=0&rc=OGVoNGc7ZmVkNDlpOTwzNUBpamx1Mzs6Zjw2OjMzNGkzM0BhMzY0L15fXzYxNjZeXzZfYSNscC0tcjRfZWNgLS1kLS9zcw%3D%3D&btag=e000a0000&dy_q=1693465014&l=202308311456549CFCC3448902F10F01AF", "https://api-play.amemv.com/aweme/v1/play/?video_id=v0200fg10000c7f3h9bc77u8000rsiog&line=0&file_id=b290b9a69f96419abbbca82d719e6bd5&sign=e31fba27444fe97a8c2b4d9007eea78f&is_play_url=1&source=PackSourceEnum_AWEME_DETAIL", "https://api.amemv.com/aweme/v1/play/?video_id=v0200fg10000c7f3h9bc77u8000rsiog&line=1&file_id=b290b9a69f96419abbbca82d719e6bd5&sign=e31fba27444fe97a8c2b4d9007eea78f&is_play_url=1&source=PackSourceEnum_AWEME_DETAIL"], "width": 576}, "play_addr_265": {"data_size": 2895492, "file_cs": "c:0-41561-11ab|d:0-1447745-15c1,1447746-2895491-8c42|a:v0200fg10000c7f3h9bc77u8000rsiog", "file_hash": "c06ca8dfb8d6b00d56be2f1c6bd019f0", "height": 1024, "uri": "v0200fg10000c7f3h9bc77u8000rsiog", "url_key": "v0200fg10000c7f3h9bc77u8000rsiog_bytevc1_540p_473206", "url_list": ["https://v11-coldf.douyinvod.com/f3e623a2956cea90f1c156652786cb61/64f047f6/video/tos/cn/tos-cn-ve-15-alinc2/f2259bcaa0e345b4a2444907ff022ca3/?a=1128&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=462&bt=462&cs=2&ds=6&ft=GNvhKpVVywSWRso80mo~ySqTeaApxVxV6vrK983lSto0g3&mime_type=video_mp4&qs=11&rc=aTU3ZGU5PDU6OTQ7NjlmM0Bpamx1Mzs6Zjw2OjMzNGkzM0BfLl4yM2JeNi8xMjVfLTY2YSNscC0tcjRfZWNgLS1kLS9zcw%3D%3D&btag=e000a0000&dy_q=1693465014&l=202308311456549CFCC3448902F10F01AF", "https://v99-coldx.douyinvod.com/74848bfac5bc2f8256d40f80313d6390/64f047f6/video/tos/cn/tos-cn-ve-15-alinc2/f2259bcaa0e345b4a2444907ff022ca3/?a=1128&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=462&bt=462&cs=2&ds=6&ft=GNvhKpVVywSWRso80mo~ySqTeaApxVxV6vrK983lSto0g3&mime_type=video_mp4&qs=11&rc=aTU3ZGU5PDU6OTQ7NjlmM0Bpamx1Mzs6Zjw2OjMzNGkzM0BfLl4yM2JeNi8xMjVfLTY2YSNscC0tcjRfZWNgLS1kLS9zcw%3D%3D&btag=e000a0000&dy_q=1693465014&l=202308311456549CFCC3448902F10F01AF", "https://api-play.amemv.com/aweme/v1/play/?video_id=v0200fg10000c7f3h9bc77u8000rsiog&line=0&file_id=909c06b38851462792a9e66b5aa412bf&sign=c06ca8dfb8d6b00d56be2f1c6bd019f0&is_play_url=1&source=PackSourceEnum_AWEME_DETAIL", "https://api.amemv.com/aweme/v1/play/?video_id=v0200fg10000c7f3h9bc77u8000rsiog&line=1&file_id=909c06b38851462792a9e66b5aa412bf&sign=c06ca8dfb8d6b00d56be2f1c6bd019f0&is_play_url=1&source=PackSourceEnum_AWEME_DETAIL"], "width": 576}, "play_addr_h264": {"data_size": 9104818, "file_cs": "c:0-53722-c2e0|d:0-4552408-a641,4552409-9104817-6638|a:v0200fg10000c7f3h9bc77u8000rsiog", "file_hash": "e31fba27444fe97a8c2b4d9007eea78f", "height": 1024, "uri": "v0200fg10000c7f3h9bc77u8000rsiog", "url_key": "v0200fg10000c7f3h9bc77u8000rsiog_h264_540p_1491492", "url_list": ["https://v9-cold1.douyinvod.com/646073a0cbbe1c2144061100a718d022/64f047f6/video/tos/cn/tos-cn-ve-15-alinc2/1e047e56b0d14d7395ea49ddb547e134/?a=1128&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1456&bt=1456&cs=0&ds=6&ft=GNvhKpVVywSWRso80mo~ySqTeaApxVxV6vrK983lSto0g3&mime_type=video_mp4&qs=0&rc=OGVoNGc7ZmVkNDlpOTwzNUBpamx1Mzs6Zjw2OjMzNGkzM0BhMzY0L15fXzYxNjZeXzZfYSNscC0tcjRfZWNgLS1kLS9zcw%3D%3D&btag=e000a0000&dy_q=1693465014&l=202308311456549CFCC3448902F10F01AF", "https://v11-cold.douyinvod.com/e9b5cbfa8961978c8b290fc39b736d33/64f047f6/video/tos/cn/tos-cn-ve-15-alinc2/1e047e56b0d14d7395ea49ddb547e134/?a=1128&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1456&bt=1456&cs=0&ds=6&ft=GNvhKpVVywSWRso80mo~ySqTeaApxVxV6vrK983lSto0g3&mime_type=video_mp4&qs=0&rc=OGVoNGc7ZmVkNDlpOTwzNUBpamx1Mzs6Zjw2OjMzNGkzM0BhMzY0L15fXzYxNjZeXzZfYSNscC0tcjRfZWNgLS1kLS9zcw%3D%3D&btag=e000a0000&dy_q=1693465014&l=202308311456549CFCC3448902F10F01AF", "https://api-play.amemv.com/aweme/v1/play/?video_id=v0200fg10000c7f3h9bc77u8000rsiog&line=0&file_id=b290b9a69f96419abbbca82d719e6bd5&sign=e31fba27444fe97a8c2b4d9007eea78f&is_play_url=1&source=PackSourceEnum_AWEME_DETAIL", "https://api.amemv.com/aweme/v1/play/?video_id=v0200fg10000c7f3h9bc77u8000rsiog&line=1&file_id=b290b9a69f96419abbbca82d719e6bd5&sign=e31fba27444fe97a8c2b4d9007eea78f&is_play_url=1&source=PackSourceEnum_AWEME_DETAIL"], "width": 576}, "ratio": "540p", "width": 1080}, "video_game_data_channel_config": {}, "video_labels": null, "video_tag": [{"level": 1, "tag_id": 2012, "tag_name": "居家"}, {"level": 2, "tag_id": 2012001, "tag_name": "装修设计"}, {"level": 3, "tag_id": 2012001001, "tag_name": "室内装修效果"}], "video_text": [], "voice_modify_id_list": null, "vtag_search": {"vtag_delay_ts": 24426, "vtag_enable": true}, "yumme_recreason": null}, "log_pb": {"impr_id": "202308311456549CFCC3448902F10F01AF"}, "status_code": 0}

```
# 更新时间 2023-11-14
```CSDN``` 侵权不让发，故在这里记录一下:
我发现很多朋友来找我咨询，然而还是不会使用，所以我打算直接开发相关接口，这段时间请大家不要加我联系方式谢谢。开发完成，我会在这边记录并更新

# 更新时间 2023-11-21
已经慢慢开发接口了，最近时间不是很充裕, 大伙儿不用着急

链接: https://apifox.com/apidoc/shared-5f13efa0-017a-4b17-8cdc-e7ea0f450ab7  访问密码: JQDa4ZbD
