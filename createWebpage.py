# Creation of Hacker News Top Articles page


def create_webpage(input):
    f = open("index.html", "w")
    message = f"""<html>
    <head>
    <title>Top_Hacker_news_articles</title> <meta charset="utf-8"> <meta name="viewport" 
    content="width=device-width, initial-scale=1, shrink-to-fit=no"> <link rel="stylesheet" 
    href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" 
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous"> 
    </head>
    <body>
    <div class="text-center">
    <h1 class="card-title">100_pages_of_top_Hacker_news_articles</h1>
    <ul class="list-group">{input}</ul>
    <script  src="https://code.jquery.com/jquery-3.2.1.slim.min.js" 
    integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" 
    crossorigin="anonymous"></script> <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper
    .min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" 
    crossorigin="anonymous"></script> <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min
    .js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" 
    crossorigin="anonymous"></script>
    </div>
    </body>
    </html> """
    f.write(message)
    f.close()


def webpage_formatted_data(data):
    title = ''
    link = ''
    f_list = []
    f_data = ''
    for line in data:
        if line[:5] == 'title':
            title = line[7: -1]
        if line[:4] == 'link':
            link = line[5: -1]
        if line[:5] == 'votes':
            votes = line[0: -1]
            vote = int(votes[7:])
            color = 'list-group-item-secondary'
            if vote >= 1000:
                color = 'list-group-item-success'
            elif vote >= 500:
                color = 'list-group-item-danger'
            elif vote >= 250:
                color = 'list-group-item-warning'
            html_code = f'<li><a href=\"{link}\" class=\"list-group-item {color}\" target=\"_blank\">{title}  ' \
                        f'<span class="badge badge-primary badge-pill">{vote}</span></a></li> '
            f_list.append(html_code)
    f_data = f_data.join(f_list)
    return f_data


with open('100_pages_of_top_Hacker_news_articles.txt', mode='r') as my_file:
    data = my_file.readlines()
    formatted_data = webpage_formatted_data(data)
    create_webpage(formatted_data)
