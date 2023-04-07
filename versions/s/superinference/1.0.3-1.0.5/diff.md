# Comparing `tmp/superinference-1.0.3.tar.gz` & `tmp/superinference-1.0.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "superinference-1.0.3.tar", last modified: Wed Mar 22 03:38:53 2023, max compression
+gzip compressed data, was "superinference-1.0.5.tar", last modified: Fri Apr  7 05:45:49 2023, max compression
```

## Comparing `superinference-1.0.3.tar` & `superinference-1.0.5.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxrwxrwx   0        0        0        0 2023-03-22 03:38:53.525583 superinference-1.0.3/
--rw-rw-rw-   0        0        0     1069 2023-03-21 13:42:01.000000 superinference-1.0.3/LICENSE.txt
--rw-rw-rw-   0        0        0     2258 2023-03-22 03:38:53.525583 superinference-1.0.3/PKG-INFO
--rw-rw-rw-   0        0        0      817 2023-03-21 13:42:01.000000 superinference-1.0.3/README.md
--rw-rw-rw-   0        0        0       97 2023-03-21 13:42:01.000000 superinference-1.0.3/pyproject.toml
--rw-rw-rw-   0        0        0      531 2023-03-22 03:38:53.529773 superinference-1.0.3/setup.cfg
-drwxrwxrwx   0        0        0        0 2023-03-22 03:38:53.471103 superinference-1.0.3/src/
-drwxrwxrwx   0        0        0        0 2023-03-22 03:38:53.502984 superinference-1.0.3/src/superinference/
--rw-rw-rw-   0        0        0        0 2023-03-21 09:18:24.000000 superinference-1.0.3/src/superinference/__init__.py
--rw-rw-rw-   0        0        0     1095 2023-03-22 03:35:34.000000 superinference-1.0.3/src/superinference/devto.py
--rw-rw-rw-   0        0        0    21524 2023-03-22 03:19:42.000000 superinference-1.0.3/src/superinference/github.py
-drwxrwxrwx   0        0        0        0 2023-03-22 03:38:53.522523 superinference-1.0.3/src/superinference.egg-info/
--rw-rw-rw-   0        0        0     2258 2023-03-22 03:38:53.000000 superinference-1.0.3/src/superinference.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      314 2023-03-22 03:38:53.000000 superinference-1.0.3/src/superinference.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-03-22 03:38:53.000000 superinference-1.0.3/src/superinference.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       15 2023-03-22 03:38:53.000000 superinference-1.0.3/src/superinference.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-07 05:45:48.993099 superinference-1.0.5/
+-rw-rw-rw-   0        0        0     1069 2023-03-21 13:42:01.000000 superinference-1.0.5/LICENSE.txt
+-rw-rw-rw-   0        0        0    11544 2023-04-07 05:45:48.994454 superinference-1.0.5/PKG-INFO
+-rw-rw-rw-   0        0        0    10103 2023-04-07 04:27:04.000000 superinference-1.0.5/README.md
+-rw-rw-rw-   0        0        0       97 2023-03-21 13:42:01.000000 superinference-1.0.5/pyproject.toml
+-rw-rw-rw-   0        0        0      531 2023-04-07 05:45:48.998459 superinference-1.0.5/setup.cfg
+drwxrwxrwx   0        0        0        0 2023-04-07 05:45:48.944921 superinference-1.0.5/src/
+drwxrwxrwx   0        0        0        0 2023-04-07 05:45:48.974171 superinference-1.0.5/src/superinference/
+-rw-rw-rw-   0        0        0        0 2023-03-21 09:18:24.000000 superinference-1.0.5/src/superinference/__init__.py
+-rw-rw-rw-   0        0        0     1095 2023-03-22 03:35:34.000000 superinference-1.0.5/src/superinference/devto.py
+-rw-rw-rw-   0        0        0    24947 2023-04-07 04:24:26.000000 superinference-1.0.5/src/superinference/github.py
+drwxrwxrwx   0        0        0        0 2023-04-07 05:45:48.990851 superinference-1.0.5/src/superinference.egg-info/
+-rw-rw-rw-   0        0        0    11544 2023-04-07 05:45:48.000000 superinference-1.0.5/src/superinference.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      314 2023-04-07 05:45:48.000000 superinference-1.0.5/src/superinference.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 05:45:48.000000 superinference-1.0.5/src/superinference.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       15 2023-04-07 05:45:48.000000 superinference-1.0.5/src/superinference.egg-info/top_level.txt
```

### Comparing `superinference-1.0.3/LICENSE.txt` & `superinference-1.0.5/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `superinference-1.0.3/setup.cfg` & `superinference-1.0.5/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 00000000: 5b6d 6574 6164 6174 615d 0d0a 6e61 6d65  [metadata]..name
 00000010: 203d 2073 7570 6572 696e 6665 7265 6e63   = superinferenc
 00000020: 650d 0a76 6572 7369 6f6e 203d 2031 2e30  e..version = 1.0
-00000030: 2e33 0d0a 6465 7363 7269 7074 696f 6e20  .3..description 
+00000030: 2e35 0d0a 6465 7363 7269 7074 696f 6e20  .5..description 
 00000040: 3d20 5375 7065 7269 6e66 6572 656e 6365  = Superinference
 00000050: 2069 7320 6120 6c69 6272 6172 7920 7468   is a library th
 00000060: 6174 2069 6e66 6572 7320 616e 616c 7973  at infers analys
 00000070: 6973 2d72 6561 6479 2061 7474 7269 6275  is-ready attribu
 00000080: 7465 7320 6672 6f6d 2061 2070 6572 736f  tes from a perso
 00000090: 6e27 2773 2073 6f63 6961 6c20 6d65 6469  n''s social medi
 000000a0: 6120 7573 6572 6e61 6d65 206f 7220 756e  a username or un
```

### Comparing `superinference-1.0.3/src/superinference/devto.py` & `superinference-1.0.5/src/superinference/devto.py`

 * *Files identical despite different names*

### Comparing `superinference-1.0.3/src/superinference/github.py` & `superinference-1.0.5/src/superinference/github.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 import requests
 import re
-from datetime import datetime
+from datetime import datetime, timedelta
 from base64 import b64decode
 from rich.console import Console
 from rich.theme import Theme
 
 console = Console(theme=Theme({"repr.str":"#54A24B", "repr.number": "#FF7F0E", "repr.none":"#808080"}))
 
 class GithubProfile:
@@ -16,145 +16,186 @@
             access_token (str, optional): Github access token to increase API rate limit and access private repositories. Defaults to None.
         """
         self.username = username
         self.access_token = access_token
         self.inference = None
         self._api_url = "https://api.github.com"
 
+    def _error_handling(self, response, graphql=False):
+        """Handles errors from the Github API
+
+        Args:
+            response (requests.models.Response): Response from the Github API
+
+        Returns:
+            requests.models.Response: Response from the Github API, if no errors are found
+        """
+        if response.status_code == 200:
+            if graphql:
+                json_data = response.json()
+                if "errors" in json_data and json_data["errors"][0]["message"]:
+                    raise Exception(f"GraphQL API query error - \"{json_data['errors'][0]['message']}\"")
+            return response
+        elif response.status_code == 401:
+            if self.access_token:    
+                raise Exception("Invalid access token. Please check your access token and try again.")
+            else:
+                raise Exception("This feature requires an access token. Please provide an access token and try again.")
+        elif response.status_code == 403:
+            if self.access_token:
+                raise Exception("API rate limit exceeded, please try again later.")
+            else:
+                raise Exception("API rate limit exceeded, please provide an access token to increase rate limit.")
+        elif response.status_code == 404:
+            raise Exception("Invalid GitHub username inputted.")
+        else:
+            raise Exception(f"Error with status code of: {response.status_code}")
+        
     def _request(self, url, error_handling=True):
         """Makes a request to the Github API
 
         Args:
             url (str): URL to be requested
             error_handling (bool, optional): Whether to handle errors or not before returning the response. Defaults to True.
 
         Returns:
-            str: Response from the API
+            requests.models.Response: Response from the Github API
         """
         if self.access_token:
             headers = {"Authorization": "token {}".format(self.access_token)}
             response = requests.get(url, headers=headers)
         else:
             response = requests.get(url)
             
         if error_handling:
-            if response.status_code == 200:
-                return response
-            elif response.status_code == 401:
-                if self.access_token:    
-                    raise Exception("Invalid access token. Please check your access token and try again.")
-                else:
-                    raise Exception("This feature requires an access token. Please provide an access token and try again.")
-            elif response.status_code == 403:
-                if self.access_token:
-                    raise Exception("API rate limit exceeded, please try again later.")
-                else:
-                    raise Exception("API rate limit exceeded, please provide an access token to increase rate limit.")
-            elif response.status_code == 404:
-                raise Exception("Invalid GitHub username inputted.")
-            else:
-                raise Exception(f"Error with status code of: {response.status_code}")
+            return self._error_handling(response)
         else:
             return response
     
     def _parse_next_link(self, headers):
         """Parses the next link from the Github API response headers
 
         Args:
             headers (dict): Response headers from the Github API
 
         Returns:
-            str: Next link
+            str: Next link to be requested
         """
         if "Link" in headers:
             links = headers["Link"]
             if 'rel="next"' in links:
                 next_link = links.split('rel="next"')[0].strip('<>; ')
                 return next_link
             else:
                 return None
         else:
             return None
     
-    def _multipage_request(self, url, item_name="items", json_key=None):
+    def _multipage_request(self, url, json_key=None):
         """Makes a request to the Github API and handles pagination
 
         Args:
             url (str): URL to be requested
-            item_name (str, optional): Name of the items requested, will be used in the message. Defaults to "items".
             json_key (str, optional): Key of the items in the JSON response. Defaults to None.
 
         Returns:
-            list: List of items
+            item_list (list): List of combined items from all pages
+            incomplete_results (bool): Whether the results are incomplete or not (due to hitting rate limits)
+            total_count (int): The total count of items for search queries. Only returned for search endpoints.
+        
         """
+        incomplete_results = False
         item_list = []
-        message = None
+        is_search = "/search/" in url
+        
         while url:
             response = self._request(url)
             if json_key:
                 item_list.extend(response.json()[json_key])
             else:
                 item_list.extend(response.json())
             url = self._parse_next_link(response.headers)
             remaining_rate = int(response.headers["X-Ratelimit-Remaining"])
             if url and remaining_rate == 0:
-                message = f"Hey there! Looks like the inference above is from the latest {len(item_list)} {item_name} since you've reached the API rate limit 😉."
+                incomplete_results = True
                 url = None
-        return item_list, message
+        if is_search:
+            total_count = response.json()["total_count"]
+            return item_list, incomplete_results, total_count
+        else:
+            return item_list, incomplete_results
     
     def _username_token_check(self):
         """Checks if the Github username is associated with the provided access token, which is called when the user wants to include private repositories"""
         test_url = f"{self._api_url}/user"
         response = self._request(test_url)
         associated_username = response.json()['login']
         if associated_username != self.username:
             raise Exception("If you want to include private repositories, please ensure that the Github username is associated with the provided access token.")
         
+    def _graphql_request(self, query):
+        """Makes a request to the Github GraphQL API
+
+        Args:
+            query (str): GraphQL query to be requested
+
+        Returns:
+            requests.models.Response: Response from the Github GraphQL API
+        """
+        url = f"{self._api_url}/graphql"
+        if self.access_token:
+            headers = {"Authorization": "token {}".format(self.access_token)}
+            response = requests.post(url, headers=headers, json={"query": query})
+        else:
+            response = requests.post(url)
+        return self._error_handling(response, graphql=True)
+        
     def _profile_inference(self):
         """Infer data regarding the user's Github profile
 
         Returns:
-            dict: Github profile data
+            dict: Github profile data and creation date
         """
         profile_url = f"{self._api_url}/users/{self.username}"
         response = self._request(profile_url)
-        profile_data = response.json()
-        return {
-            "login": profile_data["login"],
-            "name": profile_data["name"],
-            "company": profile_data["company"],
-            "blog": profile_data["blog"],
-            "location": profile_data["location"],
-            "email": profile_data["email"],
-            "hireable": profile_data["hireable"],
-            "twitter_username": profile_data["twitter_username"],
-            "avatar_url": profile_data["avatar_url"],
-            "bio": profile_data["bio"],
-            "followers": profile_data["followers"],
-            "following": profile_data["following"]
+        json_data = response.json()
+        profile_data =  {
+            "login": json_data["login"],
+            "name": json_data["name"],
+            "company": json_data["company"],
+            "blog": json_data["blog"],
+            "location": json_data["location"],
+            "email": json_data["email"],
+            "hireable": json_data["hireable"],
+            "twitter_username": json_data["twitter_username"],
+            "avatar_url": json_data["avatar_url"],
+            "bio": json_data["bio"],
+            "followers": json_data["followers"],
+            "following": json_data["following"]
         }
+        return {"data": profile_data, "created_at": json_data['created_at']}
     
 
     def _repository_inference(self, top_repo_n=3, include_private=False):
         """Infer data regarding the user's Github repositories
 
         Args:
             top_repo_n (int, optional): Number of top repositories to be included in the inference. Defaults to 3.
             include_private (bool, optional): Whether to include private repositories in the inference. Defaults to False.
 
         Returns:
-            dict: Github repository data and statistics
+            dict: Github repository statistics and list of original repositories
         """
         if include_private:
             self._username_token_check()
             repo_url = f"{self._api_url}/user/repos?per_page=100"
         else:
             repo_url = f"{self._api_url}/users/{self.username}/repos?per_page=100"
             
-        repos, repo_message = self._multipage_request(repo_url, "repos")
+        repos, incomplete_results = self._multipage_request(repo_url)
 
         repos.sort(
             key=lambda r: r["stargazers_count"] + r["forks_count"],
             reverse=True,
         )
 
         original_repos, forked_repos = [], []
@@ -179,195 +220,237 @@
                     "top_language": r["language"],
                     "stargazers_count": r["stargazers_count"],
                     "forks_count": r["forks_count"],
                 }
             )
 
         stats = {
+            "incomplete_repo_results": incomplete_results,
+            "inference_from_repo_count": len(repos),
             "original_repo_count": len(original_repos),
             "forked_repo_count": len(forked_repos),
             "counts": counts,
             "top_repo_stars_forks": popular_repos,
         }
 
-        return {"stats": stats, "original_repos": original_repos, "repos": repos, "repo_api_message": repo_message}
+        return {"stats": stats, "original_repos": original_repos}
     
-    def _contribution_inference(self, include_private=False):
-        """Infer data regarding the user's Github contributions (issues and pull requests)
+    def _contribution_inference(self, created_profile_date, original_repos):
+        """Infers data regarding a user's contributions to repositories on GitHub.
 
         Args:
-            include_private (bool, optional): Whether to include private repositories in the inference. Defaults to False.
+            created_profile_date (str): The user's Github profile creation date (from `_profile_inference()`)
+            original_repos (list): Original repository data (from `_repository_inference()`)
 
         Returns:
-            dict: Github contribution data and statistics
+            dict: Github contribution statistics
         """
-        if include_private:
-            self._username_token_check()
-            issue_url = f"{self._api_url}/search/issues?q=type:issue author:{self.username}&sort=author-date&order=desc&per_page=100"
-            pr_url = f"{self._api_url}/search/issues?q=type:pr author:{self.username}&sort=author-date&order=desc&per_page=100"
-        else:
-            issue_url = f"{self._api_url}/search/issues?q=type:issue author:{self.username} is:public&sort=author-date&order=desc&per_page=100"
-            pr_url = f"{self._api_url}/search/issues?q=type:pr author:{self.username} is:public&sort=author-date&order=desc&per_page=100"
-            
-        issue_data, issue_message = self._multipage_request(issue_url, "issues", "items")
-        pr_data, pr_message = self._multipage_request(pr_url, "PRs", "items")
-        issues, prs = [], []
-
-        for i in issue_data:
-            if i['author_association'] != 'OWNER':
-                split_url = i['html_url'].split('/')
-                issues.append({
-                    'issue_title': i['title'],
-                    'created_at': i['created_at'],
-                    'state': i['state'],
-                    'state_reason': i['state_reason'],
-                    'repo_owner': split_url[3],
-                    'repo_name': split_url[4],
-                    'repo_url': f'https://github.com/{split_url[3]}/{split_url[4]}'
-                })
-
-        for p in pr_data:
-            if p['author_association'] != 'OWNER':
-                split_url = p['html_url'].split('/')
-                prs.append({
-                    'pr_title': p['title'],
-                    'created_at': p['created_at'],
-                    'merged_at': p['pull_request']['merged_at'],
-                    'state': p['state'],
-                    'state_reason': p['state_reason'],
-                    'repo_owner': split_url[3],
-                    'repo_name': split_url[4],
-                    'repo_url': f'https://github.com/{split_url[3]}/{split_url[4]}'
-                })
-                
-        merged_pr_count = len([p for p in prs if p['merged_at']])
-
-        contribution_count = {}
-        for ip in issues + prs:
-            repo_owner = ip['repo_owner']
-            contribution_count[repo_owner] = contribution_count.get(repo_owner, 0) + 1
-
-        contribution_count = dict(sorted(contribution_count.items(), key=lambda x: x[1], reverse=True))
+        if not self.access_token:
+            return None
         
-        contribution = {
-                        'issue_count': len(issues),
-                        'total_pr_count': len(prs),
-                        'merged_pr_count': merged_pr_count,
-                        'contribution_count_per_repo_owner': contribution_count,
-                        'created_issue': issues,
-                        'created_pr': prs,
-                        'issue_api_message': issue_message,
-                        'pr_api_message': pr_message
-                        }
-
-        return {'contribution': contribution, 'issue_api_message': issue_message, 'pr_api_message': pr_message}
-    
-    def _activity_inference(self, original_repos, top_repo_n=3, include_private=False):
-        """Infer data regarding the user's Github activity (commits)
-
-        Args:
-            original_repos (dict): Original repository data (from _repo_inference)
-            top_repo_n (int, optional): Number of top repositories to be included in the inference. Defaults to 3.
-            include_private (bool, optional): Whether to include private repositories in the inference. Defaults to False.
-
-        Returns:
-            dict: Github activity data and statistics
+        created_date = datetime.strptime(created_profile_date, "%Y-%m-%dT%H:%M:%SZ")
+        created_year = created_date.year
+        today = datetime.now()
+        current_year = today.year
+        
+        def query_pattern_day(start_date, end_date):
+            return f"""
+                query {{
+                    user(login: "{self.username}") {{
+                        contributionsCollection(from: "{start_date.isoformat()}", to: "{end_date.isoformat()}") {{
+                            contributionCalendar {{
+                                totalContributions
+                                weeks {{
+                                    contributionDays {{
+                                        date
+                                        contributionCount
+                                    }}
+                                }}
+                            }}
+                        }}
+                    }}
+                }}
+            """
+        
+        contribution_detail = """
+            repository {
+                description
+                name
+                url
+                languages(first: 1, orderBy: {field: SIZE, direction: DESC}) {
+                    nodes {
+                        name
+                    }
+                }
+                owner {
+                    __typename
+                    ... on User {
+                        login
+                    }
+                    ... on Organization {
+                        login
+                    }
+                }
+            }
+            contributions {
+                totalCount
+            }
         """
-        if include_private:
-            self._username_token_check()
-            commit_url = self._api_url + f"/search/commits?q=committer:{self.username}&sort=committer-date&order=desc&per_page=100"
-        else:
-            commit_url = self._api_url + f"/search/commits?q=committer:{self.username} is:public&sort=committer-date&order=desc&per_page=100"
-        commit_data, commit_message = self._multipage_request(commit_url, "commits", "items")
+        
+        def query_pattern_repo(start_date, end_date):
+            return f"""
+                query {{
+                    user(login: "{self.username}") {{
+                        contributionsCollection(from: "{start_date.isoformat()}", to: "{end_date.isoformat()}") {{
+                            commitContributionsByRepository(maxRepositories: 100) {{
+                                {contribution_detail}
+                            }}
+                            issueContributionsByRepository(maxRepositories: 100) {{
+                                {contribution_detail}
+                            }}
+                            pullRequestContributionsByRepository(maxRepositories: 100) {{
+                                {contribution_detail}
+                            }}
+                            pullRequestReviewContributionsByRepository(maxRepositories: 100) {{
+                                {contribution_detail}
+                            }}
+                        }}
+                    }}
+                }}
+            """
+        
+        contributions_per_day = []
+        contributions_per_repo = []
+        contributions_count = 0
+        for i in range(created_year, current_year + 1):
+            if i == created_year:
+                query_day = query_pattern_day(created_date, datetime(i, 12, 31))
+                query_repo = query_pattern_repo(created_date, datetime(i, 12, 31))
+            elif i == current_year:
+                query_day = query_pattern_day(datetime(i, 1, 1), today)
+                query_repo = query_pattern_repo(datetime(i, 1, 1), today)
+            else:
+                query_day = query_pattern_day(datetime(i, 1, 1), datetime(i, 12, 31))
+                query_repo = query_pattern_repo(datetime(i, 1, 1), datetime(i, 12, 31))
 
-        commits = []
-        for c in commit_data:
-            commits.append({
-            "created_at": c["commit"]["committer"]["date"][:10],
-            "repo_owner": c["repository"]["owner"]["login"],
-            "repo_owner_type": c["repository"]["owner"]["type"],
-            "repo_name": c["repository"]["name"]})
-
-        counts = {
-            "date": {},
-            "day": {},
-            "month": {},
+            response_day = self._graphql_request(query_day)
+            data_day = response_day.json()['data']
+            new_contribution_day=[]
+            for week in data_day["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]:
+                new_contribution_day.extend([day for day in week["contributionDays"]])
+            contributions_per_day.extend(new_contribution_day)
+            contributions_count += data_day["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"]
+
+            response_repo = self._graphql_request(query_repo)
+            data_repo = response_repo.json()['data']
+            def extract_repo_detail(repository, contributions):
+                return {
+                    "name": repository['name'],
+                    "owner": repository['owner']['login'],
+                    "owner_type": repository['owner']["__typename"],
+                    "html_url": repository['url'],
+                    "description": repository['description'],
+                    "top_language": repository['languages']['nodes'][0]['name'].lower().replace(" ", "-") if repository['languages']['nodes'] else None,
+                    "contributions_count": contributions['totalCount']
+                }
+            new_commits = [extract_repo_detail(item['repository'], item['contributions']) for item in data_repo['user']['contributionsCollection']['commitContributionsByRepository']]
+            new_issues = [extract_repo_detail(item['repository'], item['contributions']) for item in data_repo['user']['contributionsCollection']['issueContributionsByRepository']]
+            new_pr = [extract_repo_detail(item['repository'], item['contributions']) for item in data_repo['user']['contributionsCollection']['pullRequestContributionsByRepository']]
+            new_pr_review = [extract_repo_detail(item['repository'], item['contributions']) for item in data_repo['user']['contributionsCollection']['pullRequestReviewContributionsByRepository']]
+            contributions_per_repo.extend(new_commits + new_issues + new_pr + new_pr_review)
+            
+        one_year_ago = datetime.now() - timedelta(days=365)
+        count = {"day": {}, "month": {}}
+        for c in contributions_per_day:
+            c_date = datetime.strptime(c["date"], "%Y-%m-%d")
+            c_day = c_date.strftime("%a")
+            c_month = c_date.strftime("%b")
+            is_one_year_ago = c_date >= one_year_ago
+            
+            count["day"][c_day] = count["day"].get(c_day, [0, 0])
+            if is_one_year_ago:
+                count["day"][c_day][0] += c['contributionCount']
+            count["day"][c_day][1] +=  c['contributionCount']
+            
+            count["month"][c_month] = count["month"].get(c_month, [0, 0])
+            if is_one_year_ago:
+                count["month"][c_month][0] += c['contributionCount']
+            count["month"][c_month][1] += c['contributionCount']
+            
+        final_count = {
+            "day": count["day"],
+            "month": count["month"],
             "owned_repo": {},
-            "other_repo": {},
-            "repo_org_owner": {},
-            "repo_user_owner": {},
+            "other_repo": [],
+            "User": {},
+            "Organization": {},
         }
-        for c in commits:
-            c_date = c["created_at"]
-            c_day = datetime.strptime(c_date, "%Y-%m-%d").strftime("%a")
-            c_month = datetime.strptime(c_date, "%Y-%m-%d").strftime("%b")
-            counts["date"][c_date] = counts["date"].get(c_date, 0) + 1
-            counts["day"][c_day] = counts["day"].get(c_day, 0) + 1
-            counts["month"][c_month] = counts["month"].get(c_month, 0) + 1
-            repo_owner, repo_owner_type, repo_name = c["repo_owner"], c["repo_owner_type"], c["repo_name"]
-            if repo_owner == self.username:
-                counts["owned_repo"][repo_name] = counts["owned_repo"].get(repo_name, 0) + 1
-            else:
-                counts["other_repo"][repo_name] = counts["other_repo"].get(repo_name, 0) + 1
-            if repo_owner_type == "Organization":
-                counts["repo_org_owner"][repo_owner] = counts["repo_org_owner"].get(repo_owner, 0) + 1
-            else:
-                counts["repo_user_owner"][repo_owner] = counts["repo_user_owner"].get(repo_owner, 0) + 1
         
-        sorted_counts = {}
-        for k in counts:
-            if k == 'date':
-                sorted_counts[k] = counts[k]
+        for c in contributions_per_repo:
+            repo_type = "owned_repo" if c['owner'] == self.username else "other_repo"
+
+            if repo_type == "owned_repo":
+                final_count[repo_type][c['name']] = final_count[repo_type].get(c['name'], 0) + c['contributions_count']
             else:
-                sorted_counts[k] = dict(sorted(counts[k].items(), key=lambda x: x[1], reverse=True))
-                
-        most_active_repo_name = list(sorted_counts['owned_repo'].keys())[:top_repo_n]
-        most_active_repo = []
-        for r in original_repos:
-            if r['name'] in most_active_repo_name:
-                most_active_repo.append({
-                    'name': r['name'],
-                    'html_url': r['html_url'],
-                    'description': r['description'],
-                    'top_language': r['language'],
-                    'commits_count': sorted_counts['owned_repo'][r['name']]
-                })
-                
-        if len(commits) > 0:
-            last_commit_date = datetime.strptime(commits[0]['created_at'], '%Y-%m-%d')
-            first_commit_date = datetime.strptime(commits[-1]['created_at'], '%Y-%m-%d')
-            total_weeks = round((last_commit_date - first_commit_date).days / 7)
-            weekly_avg_commits = round(len(commits) / total_weeks, 3)
-        else:
-            weekly_avg_commits = 0
+                index = next((i for i, obj in enumerate(final_count[repo_type]) if obj["name"] == c['name']), -1)
+                if index == -1:
+                    data = {k: v for k, v in c.items() if k != "owner_type"}
+                    final_count[repo_type].append(data)             
+                else:
+                    final_count[repo_type][index]["contributions_count"] += c['contributions_count']      
+
+            final_count[c['owner_type']][c['owner']] = final_count[c['owner_type']].get(c['owner'], 0) + c['contributions_count']
             
-        activity = {
-            'commit_count': len(commits),
-            'most_active_day': list(sorted_counts['day'].keys())[0] if len(commits) > 0 else None,
-            'most_active_month': list(sorted_counts['month'].keys())[0] if len(commits) > 0 else None,
-            'weekly_average_commits': weekly_avg_commits,
-            'commit_count_per_day': sorted_counts['day'],
-            'commit_count_per_month': sorted_counts['month'],
-            'commit_count_per_owned_repo': sorted_counts['owned_repo'],
-            'commit_count_per_other_repo': sorted_counts['other_repo'],
-            'commit_count_per_repo_org_owner': sorted_counts['repo_org_owner'],
-            'commit_count_per_repo_user_owner': sorted_counts['repo_user_owner'],
-            'commit_api_message': commit_message
-        }
+        sorted_count = {}
+        for k, v in final_count.items():
+            if k == "day" or k == "month":
+                sorted_count[k] = dict(sorted(v.items(), key=lambda item: item[1][0], reverse=True))
+            elif k == "other_repo":
+                sorted_count[k] = sorted(v, key=lambda v: v["contributions_count"], reverse=True)
+            else:
+                sorted_count[k] = dict(sorted(v.items(), key=lambda item: item[1], reverse=True))
+            
+        total_weeks = round((today - created_date).days / 7)
+        weekly_avg_contributions = round(contributions_count / total_weeks, 3)
+        
+        data_contrib = []
+        for r in original_repos[:10]:
+            response = self._request(r['contributors_url'])
+            repo_data = response.json()
+            data_contrib.extend(repo_data)
+
+        incoming_contribution = {}
+        for d in data_contrib:
+            login = d['login']
+            if login != self.username:
+                incoming_contribution[login] = incoming_contribution.get(login, 0) + d['contributions']
 
-        return {'activity': activity, 'most_active_repo': most_active_repo, 'commit_api_message': commit_message}
+        sorted_incoming_contribution = dict(sorted(incoming_contribution.items(), key=lambda item: item[1], reverse=True))
+        
+        contribution = {
+            'contribution_count': contributions_count,
+            'weekly_average_contribution': weekly_avg_contributions,
+            'contribution_count_per_day': sorted_count["day"],
+            'contribution_count_per_month': sorted_count["month"],
+            'contribution_count_per_owned_repo': sorted_count["owned_repo"],
+            'contribution_count_per_other_repo': sorted_count["other_repo"],
+            'contribution_count_per_repo_org_owner': sorted_count["Organization"],
+            'contribution_count_per_repo_user_owner': sorted_count["User"],
+            'external_contribution_to_top_10_repo': sorted_incoming_contribution
+        }
+        
+        return contribution
     
-    def _skill_inference(self, bio, original_repos, repo_message, top_language_n=3):
+    def _skill_inference(self, bio, original_repos, top_language_n=3):
         """Infer data regarding the user's skills from their Github bio and repositories.
 
         Args:
             bio (str): The user's Github bio
-            original_repos (dict): Original repository data (from _repo_inference)
-            repo_message (str): Message from _repo_inference
-            top_language_n (int): Number of top languages to be included in the inference. Defaults to 3.
+            original_repos (dict): Original repository data from _repository_inference()
+            top_language_n (int, optional): The number of top languages to consider. Defaults to 3.
 
         Returns:
             dict: Inferred data regarding the user's skills
         """
         response = requests.get("https://raw.githubusercontent.com/supertypeai/collective/main/src/data/profileTagsChoices.json")
         keywords = response.json()
         
@@ -401,46 +484,50 @@
 
         languages_count = {}
         if self.access_token:
             for r in original_repos:
                 response = self._request(r["languages_url"])
                 r_lang = response.json()
                 for key in r_lang.keys():
-                    languages_count[key] = languages_count.get(key, 0) + 1
+                    formatted_key = key.replace(" ", "-").lower()
+                    languages_count[formatted_key] = languages_count.get(formatted_key, 0) + 1
             sorted_languages = sorted(languages_count, key=languages_count.get, reverse=True)
             languages_percentage = {lang: round(languages_count[lang] / len(original_repos), 3) for lang in sorted_languages}
         else:
             for r in original_repos:
-                languages_count[r["language"]] = languages_count.get(r["language"], 0) + 1
+                if r['language']:
+                    formatted_lang = r["language"].replace(" ", "-").lower()
+                    languages_count[formatted_lang] = languages_count.get(formatted_lang, 0) + 1
             sorted_languages = sorted(languages_count, key=languages_count.get, reverse=True)
-            languages_percentage = "Sorry, it looks like the information you're requesting is only available for authenticated requests 😔"
+            languages_percentage = None
         
-        return {
+        skill = {
+            "inference_from_originalrepo_count": len(original_repos),
             "key_qualifications": key_qualifications, 
             "top_n_languages": sorted_languages[:top_language_n], 
             "languages_percentage": languages_percentage,
-            "repo_api_message": repo_message
             }
+        
+        return skill
     
     def perform_inference(self, top_repo_n=3, top_language_n=3, include_private=False):
         """Perform inference on the user's Github profile. This will print out a dictionary that includes data and statistics regarding their profile, repository, skill, activity, and contribution. The dictionary will also be stored in the inference attribute.
 
         Args:
             top_repo_n (int, optional): Number of top repositories to be included in the inference. Defaults to 3.
             top_language_n (int, optional): Number of top languages to be included in the inference. Defaults to 3.
             include_private (bool, optional): Whether to include private repositories in the inference. Defaults to False.
         """
         profile = self._profile_inference()
         repository = self._repository_inference(top_repo_n=top_repo_n, include_private=include_private)
-        skill = self._skill_inference(bio=profile['bio'], original_repos=repository['original_repos'], repo_message=repository['repo_api_message'], top_language_n=top_language_n)
-        activity = self._activity_inference(original_repos=repository['original_repos'], top_repo_n=top_repo_n, include_private=include_private)
-        contribution = self._contribution_inference(include_private=include_private)
+        skill = self._skill_inference(bio=profile['data']['bio'], original_repos=repository['original_repos'], top_language_n=top_language_n)
+        contribution = self._contribution_inference(created_profile_date=profile['created_at'], original_repos=repository['original_repos'])
         
         self.inference = {
-            "profile": profile,
+            "profile": profile['data'],
             "skill": skill,
             "stats": repository["stats"],
-            "activity": activity,
+            # "activity": activity,
             "contribution": contribution
         }
         
         console.print(self.inference)
```

