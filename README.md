# Steam Game WordCloud Generator

## How it works
It firstly crawl the the comment page of a given game on Steam. Since the page is dynamic, selenium is necessary and is used to mimic the motion of scrolling down the page. After certain pages of comments have been collected, program will download and save all the comments content into a text file and then a wordcloud will be generated using wordcloud.

## Built with
* [selenium](http://selenium-python.readthedocs.io/) -Used to mimic the behavior of mouse/keyboard since steam is a dynamic website
* [PhathomJs](http://phantomjs.org/) -PhathomJS is used to render the website page
* [wordcloud](https://amueller.github.io/word_cloud/) -wordcloud is the main lib used to generate the wordcloud in this program
* [matplotlib](https://matplotlib.org/) -matplotlib is used for the display and save of wordcloud pic


## Sample
This is the result wordcloud of game NEKOPARA vol 1 on steam
![image](https://github.com/bilaer/Steam-Game-WordCloud-Generator/blob/master/figure_2.png?raw=true)
