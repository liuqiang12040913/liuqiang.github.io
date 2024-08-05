import bibtexparser


def bib_to_html(bib_file):
    with open(bib_file, 'r') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    
    def process_title(title):
        title = title.replace('{','')
        title = title.replace('}','')
        return title

    def process_author(author_strings):
        authors_output = ''
        aus = author_strings.split('and')
        if len(aus)>1:
            for au in aus:
                names = au.split(',')
                au_name = names[-1].replace(' ','') + ' ' + names[0].replace(' ','')
                authors_output += au_name + ', '
        else:
            authors_output = author_strings

        return authors_output

    html = ''
    for entry in bib_database.entries:

        title = process_title(entry['title'])
        author = process_author(entry['author'])

        conference =''
        try:
            conference = entry['booktitle']
        except: pass
        try:
            conference = entry['journal']
        except: pass
            
        first = '<ul class="myitem"><li>' + title +'</li>'
        second = '<li class="myitem_info">' + author + conference + ', ' + entry['year'] +'</li>'
        last = "</ul>"
        html+= first + second + last +'\n'

    return html

# Usage
html_content = bib_to_html('qiang.bib')

print(html_content)

# Write HTML content to a file
with open('output.html', 'w') as html_file:
    html_file.write(html_content)

print("HTML content has been written to output.html")


	# <ul class="paper">
	# 	<li >LeFi: Learn to Incentivize Federated Learning in Automotive Edge Computing</li>
	# 	<li class="paper_info">Ming Zhao, Yuru Zhang, Qiang Liu, Tao Han, IEEE Global Communications Conference (GLOBECOM), 2024</li>
	# </ul>