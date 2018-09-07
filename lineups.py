import scrapy

class LineupsSpider(scrapy.Spider):
    name = 'lineups'
    start_urls = ['http://www.baseballpress.com/lineups']
    #start_urls = ['http://www.baseballpress.com/lineups/2018-08-18']

    def parse(self, response):
        GAME_SELECTOR = '.game'

        for game in response.css(GAME_SELECTOR):
            TEAM_SELECTOR = '.team-name::text'
            PLAYER_SELECTOR = '.player-link::text'

            yield {
                'away-team': game.css(TEAM_SELECTOR).extract()[0],
                'away-pitcher': game.css(PLAYER_SELECTOR).extract()[0],
                'away-lineup': game.css(PLAYER_SELECTOR).extract()[2:11],
                'home-team': game.css(TEAM_SELECTOR).extract()[1],
                'home-pitcher': game.css(PLAYER_SELECTOR).extract()[1],
                'home-lineup': game.css(PLAYER_SELECTOR).extract()[11:20]
            }