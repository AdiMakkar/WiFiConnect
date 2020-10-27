"""
A precondition for the algorithm working is that the library 'requests'
must be installed on the device prior to using the program
"""
import requests

def auto_reconnect():
      """
      Auto reconnect to password module

      The ClientURL (cURL) command converted over to python for compatibility
      with all platforms

      The program initiates by accepting the cookies provided on the webpage
      The code opens the provided link and accepts the terms and conditions
      button 
      """
      cookies = {
          '_ga': 'GA1.2.490792435.1536769170',
      }
      headers = {
          'Host': 'conditions.bruyere.org',
          'User-Agent': 'Safari/5.0 (X11; Linux i686 on x86_64; rv:52.0) Gecko/20100101 Safari/52.0',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Accept-Language': 'en-US,en;q=0.5',
          'Referer': 'https://conditions.bruyere.org/fs/customwebauth/login.html?switch_url=https://conditions.bruyere.org/login.html&wlan=GuestWifi&statusCode=1',
          'Connection': 'keep-alive',
          'Upgrade-Insecure-Requests': '1',
      }
      data = {
        'buttonClicked': '4',
        'redirect_url': '',
        'err_flag': '0'
      }
      response = requests.post('https://conditions.bruyere.org/login.html', headers=headers, cookies=cookies, data=data)
      print("Terms and Conditions : Accepted automatically without user interference")
      #### Once the terms and conditions are accepted the algorithm prints the confirmation statement ####
       
if __name__ == '__main__':
      auto_reconnect()
