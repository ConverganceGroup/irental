
from flask import jsonify, render_template
from itsdangerous import json
from apps import db
from apps.facebook.models import Campaign as comp
from apps.facebook.models import Ads
# from .models import Results
from ..utils.helper import Helper
from apps.facebook import blueprint #as facebook_blueprint

my_access_token ="EAAEfJmDPHNQBAAFGzaYSLjA5YZBqsY2NnAJUzyCwKVR0l6QamBQGhhCA63OelTUPMoZB2hL8PEGSjtxcNOalSOdVrXQyoCIqPYcy5JlZBXBKm4VrafStG8tCvUEhiJmO0lqSnfjMg5ZAJoYDXXSP0no76WrBPzJvlhWjGy864bY47KXMJw5dmqYZBedprdkMzo9ZCv3wU58QZDZD"


from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign




@blueprint.route("/get_campaigns_data",methods=["GET"])
def get_results():
    try:
        my_app_id = '205274791646907'
        my_app_secret = '5f239d35c302458afec9fb113434ab0c'
        FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
        my_account = AdAccount('act_527655717872173')
        campaigns = my_account.get_campaigns(fields=tuple(Campaign. _field_types.keys()))
        ads = my_account.get_reach_estimate(fields=tuple())
        lst = []
        for index in range(len(campaigns)):
            obj = {}
            for key,value in campaigns[index].items():
                obj[key] = value[0] if type(value) == list  else value
            lst.append(obj)
        for item in lst:
            obj_camp =comp(**item)
            db.session.add(obj_camp)
            db.session.commit()
        return jsonify({
            "code":200,
            "status":"success",
            "message":"add campaigns successfully!"
        })
    except Exception as e:
        return jsonify(str(e))



@blueprint.route("/facebook_campagins",methods=["GET"])
def facebook_campagins():
    try:
        all_campaigns = comp.get_all_campaigns()
        #data = Helper.create_campagins_respnse(data=all_campaigns)
        return render_template("facebook/campagins.html",data=all_campaigns)
    except Exception as e:
        return jsonify(str(e))

@blueprint.route("/ads_words_credentails",methods=["GET"])
def ads_words_credentails():
    try:
        return render_template("facebook/ad_words_credentails.html")
    except Exception as e:
        return jsonify(str(e))


@blueprint.route("/instagram_credentails",methods=["GET"])
def instagram_credentails():
    try:
        return render_template("facebook/instagram_credentails.html")
    except Exception as e:
        return jsonify(str(e))



@blueprint.route("/get_all_campaigns",methods=["GET"])
def get_all_campaigns():
    try:
        all_campaigns = comp.get_all_campaigns()
        data = Helper.create_campagins_respnse(data=all_campaigns)

        return jsonify({
            "code":500,
            "status":"success",
            "message":data,
            "data":""
        })

    except Exception as e:
        return jsonify({
            "code":500,
            "status":"success",
            "message":str(e)
        })
@blueprint.route("/get_all_fbads",methods=["GET"])
def get_all_fbads():    
    try:
        all_campaigns = comp.get_all_fbads()
        data = Helper.create_fbads_respnse(data=all_fbads)

        return jsonify({
            "code":500,
            "status":"success",
            "message":data,
            "data":""
        })

    except Exception as e:
        return jsonify({
            "code":500,
            "status":"success",
            "message":str(e)
        })    