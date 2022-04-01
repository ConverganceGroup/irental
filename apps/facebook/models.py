from enum import auto
from apps import db


class Results(db.Model):
    __tablename__ = 'Results'
    id = db.Column(db.Integer, primary_key=True)
    page_reach= db.Column(db.BigInteger(), unique=True)
    source = db.Column(db.String(64), unique=True)
    date = db.Column(db.String(64), unique=True)
    

    def __str__(self)-> int:
        return self.page_reach

class Campaign(db.Model):
    __tablename__ = 'Campaign'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    account_id = db.Column(db.String(255))
    ad_strategy_id= db.Column(db.String(255))
    bid_strategy = db.Column(db.String(255))
    budget_rebalance_flag = db.Boolean(db.String(255))
    budget_remaining = db.Column(db.String(255), nullable=True)
    buying_type = db.Column(db.String(255), nullable=True)
    can_create_brand_lift_study = db.Column(db.String(255), nullable=True)
    can_use_spend_cap = db.Column(db.String(255), nullable=True)
    configured_status = db.Column(db.String(255), nullable=True)
    created_time = db.Column(db.String(255), nullable=True)
    daily_budget = db.Column(db.String(255), nullable=True)
    effective_status = db.Column(db.String(255), nullable=True)
    is_skadnetwork_attribution = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(255), nullable=True)
    objective = db.Column(db.String(255), nullable=True)
    pacing_type = db.Column(db.String(255), nullable=True)
    smart_promotion_type = db.Column(db.String(255), nullable=True)
    source_campaign_id = db.Column(db.String(255), nullable=True)
    special_ad_categories = db.Column(db.String(255), nullable=True)
    special_ad_category = db.Column(db.String(255), nullable=True)
    special_ad_category_country = db.Column(db.String(255), nullable=True)
    start_time = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(255), nullable=True)
    stop_time = db.Column(db.String(255), nullable=True)
    topline_id = db.Column(db.String(255), nullable=True)
    updated_time = db.Column(db.String(255), nullable=True)

    def __init__(self,account_id=None,ad_strategy_id=None,adlabels=None,
        bid_strategy=None ,
        boosted_object_id=None ,
        brand_lift_studies=None ,
        budget_rebalance_flag=None ,
        budget_remaining=None ,
        buying_type=None ,
        can_create_brand_lift_study=None ,
        can_use_spend_cap =None,
        configured_status=None ,
        created_time=None ,
        daily_budget=None,
        effective_status =None,
        id=None ,
        is_skadnetwork_attribution=None ,
        issues_info=None ,
        last_budget_toggling_time=None ,
        lifetime_budget=None ,
        name=None ,
        objective =None,
        pacing_type =None,
        promoted_object =None,
        recommendations =None,
        smart_promotion_type =None,
        source_campaign =None,
        source_campaign_id =None,
        special_ad_categories =None,
        special_ad_category=None ,
        special_ad_category_country =None,
        spend_cap =None,
        start_time =None,
        status =None,
        stop_time =None,
        topline_id=None ,
        updated_time=None ,
        adbatch =None,
        execution_options =None,
        iterative_split_test_configs=None ,
        upstream_events=None):
        self.account_id= account_id,
        self.ad_strategy_id = ad_strategy_id,
        self.adlabels = adlabels,
        self.bid_strategy = bid_strategy ,
        self.boosted_object_id = boosted_object_id ,
        self.brand_lift_studies = brand_lift_studies ,
        self.budget_rebalance_flag = budget_rebalance_flag,
        self.budget_remaining = budget_remaining ,
        self.buying_type = buying_type,
        self.can_create_brand_lift_study=can_create_brand_lift_study ,
        self.can_use_spend_cap=can_use_spend_cap ,
        self.configured_status=configured_status ,
        self.created_time=created_time ,
        self.daily_budget=daily_budget ,
        self.effective_status=effective_status ,
        self.id = id ,
        self.is_skadnetwork_attribution=is_skadnetwork_attribution ,
        self.issues_info=issues_info ,
        self.last_budget_toggling_time=last_budget_toggling_time ,
        self.lifetime_budget=lifetime_budget ,
        self.name=name ,
        self.objective=objective ,
        self.pacing_type=pacing_type ,
        self.promoted_object=promoted_object ,
        self.recommendations=recommendations ,
        self.smart_promotion_type=smart_promotion_type ,
        self.source_campaign=source_campaign ,
        self.source_campaign_id=source_campaign_id ,
        self.special_ad_categories=special_ad_categories ,
        self.special_ad_category=special_ad_category ,
        self.special_ad_category_country=special_ad_category_country ,
        self.spend_cap=spend_cap ,
        self.start_time=start_time ,
        self.status=status ,
        self.stop_time=stop_time ,
        self.topline_id=topline_id ,
        self.updated_time =updated_time,
        self.adbatch=adbatch ,
        self.execution_options=execution_options ,
        self.iterative_split_test_configs=iterative_split_test_configs ,
        self.upstream_events = upstream_events
        
    @staticmethod
    def get_all_campaigns():
        return Campaign.query.all()
    def __str__(self) -> str:
        return self.name

class Ads (db.Model):
    __tablename__= 'Ads'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    account_id = db.Column(db.String(255))
    ad_review_feedback = db.Column(db.String(255))
    adlabels =db.Column(db.String(255))
    adset = db.Column(db.String(255))



    def __init__(self,account_id,ad_review_feedback,adlabels,adset):
        self.account_id = account_id
        self.ad_review_feedback = ad_review_feedback
        self.adlabels = adlabels
        self.adset = adset








# class Ads(db.Models):
#     __tablename__ = 'Ads'
#     id = db.Column(db.Integer, primary_key=True,autoincrement=True)