from ds1.constants.url import URL
from ds1.resource import Resource


class Cohorts(Resource):
    def __init__(self, client):
        super().__init__(client=client)
        self.name = "Dubverse Cohorts"
        self.base_url = URL.ADMIN_PREFIX + URL.COHORTS_URL

    def list(self, cohort_name=None):
        """List all cohorts, optionally filtered by name"""
        params = {}
        if cohort_name:
            params["cohort_name"] = cohort_name
        return self.all(params=params)

    def create(self, cohort_name):
        """Create a new cohort"""
        if not cohort_name:
            raise Exception(f"Error Creating {self.name}: cohort_name is required")
        return self.post_url(self.base_url, data={"cohort_name": cohort_name})

    def update(self, cohort_id, cohort_name):
        """Update a cohort's name"""
        if not cohort_id or not cohort_name:
            raise Exception(f"Error Updating {self.name}: cohort_id and cohort_name are required")
        url = f"{self.base_url}/{cohort_id}"
        return self.put_url(url, data={"cohort_name": cohort_name})

    def add_user(self, cohort_id, user_id):
        """Add a user to a cohort"""
        if not cohort_id or not user_id:
            raise Exception(f"Error Adding User to {self.name}: cohort_id and user_id are required")
        url = f"{self.base_url}/{cohort_id}/add_user_to_cohort"
        return self.post_url(url, data={"user_id": user_id})

    def remove_user(self, cohort_id, user_id):
        """Remove a user from a cohort"""
        if not cohort_id or not user_id:
            raise Exception(f"Error Removing User from {self.name}: cohort_id and user_id are required")
        url = f"{self.base_url}/{cohort_id}/remove_user_from_cohort"
        return self.post_url(url, data={"user_id": user_id})

    def get_for_user(self, user_id):
        """Get all cohorts for a specific user"""
        if not user_id:
            raise Exception(f"Error Fetching {self.name}: user_id is required")
        
        url = f"{self.base_url}/cohorts_for_user"
        res = self.get_url(url, params={"user_id": user_id})
        if isinstance(res, list):
            return res
        else:
            raise Exception(f"Error Fetching {self.name} for User: {user_id}") 