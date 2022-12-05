
import newspaper
from newspaper import Article
import concurrent.futures
import urllib.request

import timeit

from newspaper.mthreading import Worker


URLs = ['http://www.foxnews.com/',
            'http://www.cnn.com/',
            'http://www.tagesschau.de/',
            'http://www.bbc.co.uk/',
            'https://theguardian.com',]



def get_headlines(): # define the function get_headline

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor: # uses the thread pool executor with it set to a max of 5 workers 
        {executor.submit(get_url, url): url for url in URLs}    # call the function get_url with the parameter url  and loops throught the list of urls 

def get_url(url):  # defines the funtion get_url
        
            
            result = newspaper.build(url, memoize_articles=False) # uses the newspaper module to build from the urls given from the excutor and asignes it the the result variable 
            print('\n''The headlines from %s are' % url, '\n') # prints the url that the content is comming from

            for i in range(1,6): # for loop that goes from 1 to 5 
                art = result.articles[i] # uses the results variable and to create an instance of an article and asignes it to art variable
                art.download()# download the content 
                art.parse()# parses the content 
                print(art.title)# prints the newspaper headline title 
            


    
if __name__ == '__main__':
    import timeit

    elapsed_time = timeit.timeit ("get_headlines()", setup="from __main__ import get_headlines",number=2)//2      # uses the timeit module by calculating the time take for the function get _headline to finsih 
                                                                                                                    #asigning it to the elapsed time variable
                                                                                                                    #also passing the url ans running it a number of 2 times
    print(elapsed_time)                                                                                             # prints the variable elasped time 

    
    
    