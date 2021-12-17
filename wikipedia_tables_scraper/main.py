#imports

from modules import module as md

#variables
url=input(str("Enter complete URL: "))
parser="html.parser"
csv_name=input(str("Enter the name of the exported table (CSV): "))

def main():
    soup = md.html_parsing(url,parser)
    titles = md.get_titles(soup)
    columns = md.get_columns(soup)
    df= md.get_df(columns,titles)
    df_csv=md.create_csv(df,csv_name)
    print("CSV Exported Correctly")

if __name__ == '__main__':
    main()

    