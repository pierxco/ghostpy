import requests

class FileHandler:

    def __init__(self, pid, user, password):
        self.pid = pid
        self.user = user
        self.password = password

    def get_file_list(self):
        uri = "http://staging2.osf.io"
        path = "/api/v2/nodes/" + self.pid + "/files/?provider=osfstorage&format=json"
        return requests.get(uri+path, auth=(self.user, self.password)).json()

    def get_file_url(self, file):
        file = file.replace(".", "%2E")
        uri = "http://staging2.osf.io"
        path = "/api/v2/nodes/" + self.pid + "/files/?name=" + file + "&provider=osfstorage"
        data = requests.get(uri+path, auth=(self.user, self.password)).json()
        return data['data'][0]['links'].get('self')

    def read_file(self, file):
        #url = self.get_file_url(file.get('name'))
        url = file['links'].get('self')
        response = requests.get(url, auth=(self.user, self.password))
        return response._content

    def get_posts(self, file):
        blog = self.get_file_list()['data']
        index = blog.index(filter(lambda post: post['name'] == file, blog)[0])
        prev = self.read_file(blog[index-1])
        curr = self.read_file(blog[index])
        next = self.read_file(blog[index+1])
        return prev, curr, next