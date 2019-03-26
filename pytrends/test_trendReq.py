from unittest import TestCase

from pytrends.request import TrendReq


class TestTrendReq(TestCase):

    def test__get_data(self):
        """Should use same values as in the documentation"""
        pytrend = TrendReq()
        self.assertEqual(pytrend.hl, 'en-US')
        self.assertEqual(pytrend.tz, 360)
        self.assertEqual(pytrend.geo, '')
        self.assertTrue(pytrend.cookies['NID'])

    def test_build_payload(self):
        """Should return the widgets to get data"""
        pytrend = TrendReq()
        pytrend.build_payload(kw_list=['pizza', 'bagel'])
        self.assertIsNotNone(pytrend.token_payload)

    def test__tokens(self):
        pytrend = TrendReq()
        pytrend.build_payload(kw_list=['pizza', 'bagel'])
        self.assertIsNotNone(pytrend.related_queries_widget_list)

    def test_interest_over_time(self):
        pytrend = TrendReq()
        pytrend.build_payload(kw_list=['pizza', 'bagel'])
        self.assertIsNotNone(pytrend.interest_over_time())

    def test_interest_by_region(self):
        pytrend = TrendReq()
        pytrend.build_payload(kw_list=['pizza', 'bagel'])
        self.assertIsNotNone(pytrend.interest_by_region())

    def test_related_topics(self):
        pytrend = TrendReq()
        pytrend.build_payload(kw_list=['pizza', 'bagel'])
        self.assertIsNotNone(pytrend.related_topics())

    def test_related_queries(self):
        pytrend = TrendReq()
        pytrend.build_payload(kw_list=['pizza', 'bagel'])
        self.assertIsNotNone(pytrend.related_queries())

    def test_trending_realtime(self):
        pytrend = TrendReq()
        self.assertIsNotNone(pytrend.trending_realtime())

    def test_top_daily(self):
        pytrend = TrendReq()
        self.assertIsNotNone(pytrend.top_daily())

    def test_suggestions(self):
        pytrend = TrendReq()
        pytrend.build_payload(kw_list=['pizza', 'bagel'])
        self.assertIsNotNone(pytrend.suggestions(keyword='pizza'))

    def test_get_historical_interest(self):
        from pytrends.request import TrendReq

        # Login to Google. Only need to run this once, the rest of requests will use the same session.
        pytrend = TrendReq()
        kw = ['zuckerberg', 'facebook stock']

        df = pytrend.get_historical_interest([kw[0]], year_start=2018, month_start=5, day_start=18, year_end=2019,
                                             month_end=1, day_end=5, sleep=1)

        # Retrieve terms individually so their popularity values aren't relative to each other!
        for k in kw[1:]:
            print('Retreiving', k, '...')
            dfnew1 = pytrend.get_historical_interest([k], year_start=2018, month_start=5, day_start=18, year_end=2019,
                                                     month_end=1, day_end=5, sleep=1)
            df[k] = dfnew1[k]
            print('Done with', k)
        print(df.head())
        print(df.tail())

        self.assertIsNotNone(df)
