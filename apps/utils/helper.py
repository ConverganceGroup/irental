


class Helper:
    @staticmethod
    def create_campagins_respnse(data=None):
        response = []
        for item in data:
            dt = {
                "account_id":item.account_id,
                'name':item.name,
                "ad_strategy_id":item.ad_strategy_id,
                # 'bid_strategy':item.bid_strategy,
                # 'budget_rebalance_flag':item.budget_rebalance_flag,
                'budget_remaining':item.budget_remaining,
                'buying_type':item.buying_type,
                'can_create_brand_lift_study':item.can_create_brand_lift_study



                
            }
            response.append(dt)
        return response
        # buying_type=None ,
        # can_create_brand_lift_study=None ,
        # can_use_spend_cap =None,
        # configured_status=None ,
        # created_time=None ,
        # daily_budget=None,
        # effective_status =None,
        # id=None ,
        # is_skadnetwork_attribution=None ,
        # issues_info=None ,
        # last_budget_toggling_time=None ,
        # lifetime_budget=None ,
        # name=None ,
        # objective =None,
        # pacing_type =None,
        # promoted_object =None,
        # recommendations =None,
        # smart_promotion_type =None,
        # source_campaign =None,
        # source_campaign_id =None,
        # special_ad_categories =None,
        # special_ad_category=None ,
        # special_ad_category_country =None,
        # spend_cap =None,
        # start_time =None,
        # status =None,
        # stop_time =None,
        # topline_id=None ,
        # updated_time=None ,
        # adbatch =None,
        # execution_options =None,
        # iterative_split_test_configs=None ,
        # upstream_events=None