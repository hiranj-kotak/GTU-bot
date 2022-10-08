import requests
from bs4 import BeautifulSoup


def get_url():
    page = requests.get('https://www.gtu.ac.in/AcademicCal.aspx')
    soup = BeautifulSoup(page.text, 'html.parser')
    # print(soup)
    links = soup.find_all('a')
    list = []
    for i in links:
        if 'href' in i.attrs:
            list.append(str(i.attrs['href']))
    # print(list)
    filter = []
    for j in list:
        if 'https://' in j:
            filter.append(j)
    # print(filter)
    final = []
    for i in filter:
        if "https://s3-ap-southeast-1.amazonaws.com/gtusitecirculars/uploads/" in i:
            #         i.replace(" ","%20")
            final.append(i)
    #         print(i)
    # print(final)
    # print(len(final))
    exact = []
    for i in final:
        j = i.replace(" ", "%20")
        exact.append(j)
        # print(j)
    ans=""
    j=0;
    for i in exact:
        # print(i)
        j+=1
        ans+=f"({j}) : {i}\n"
    print(ans)
    return ans
# if __name__ == '__main__':
#     get_url()


