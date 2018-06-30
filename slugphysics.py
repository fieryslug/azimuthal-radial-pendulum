import robobrowser as rb
import bs4

def main():
    browser = rb.RoboBrowser();
    browser.open('http://sebpearce.com/bullshit/')
    l = browser.get_links()[2]
    browser
    print(l)

def writeHtml(browser: rb.RoboBrowser):

    cont = str(browser.parsed)
    with open('page.html', 'w') as f:
        f.write(cont)


if __name__ == '__main__':
    main()