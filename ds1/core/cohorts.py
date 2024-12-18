from ds1.constants.url import URL
from ds1.resource import Resource


class CohortError(Exception):
    """Base exception for cohort-related errors"""
    pass


class CohortNotFoundError(CohortError):
    """Raised when a cohort cannot be found"""
    pass


class UserNotFoundError(CohortError):
    """Raised when a user cannot be found"""
    pass


class InvalidParameterError(CohortError):
    """Raised when invalid parameters are provided"""
    pass


class Cohorts(Resource):
    def __init__(self, client):
        super().__init__(client=client)
        self.name = "Dubverse Cohorts"
        self.base_url = URL.VERSION + URL.COHORTS_URL

    def list(self, cohort_name=None):
        """
        List all cohorts, optionally filtered by name
        
        Args:
            cohort_name (str, optional): Name to filter cohorts by
            
        Returns:
            list: List of cohort objects
            
        Raises:
            CohortError: If there's an error fetching the cohorts
        """
        try:
            params = {}
            if cohort_name:
                params["cohort_name"] = cohort_name
            return self.all(params=params)
        except Exception as e:
            raise CohortError(f"Failed to fetch cohorts: {str(e)}")

    def create(self, cohort_name):
        """
        Create a new cohort
        
        Args:
            cohort_name (str): Name of the cohort to create
            
        Returns:
            dict: Created cohort object
            
        Raises:
            InvalidParameterError: If cohort_name is not provided or invalid
            CohortError: If there's an error creating the cohort
        """
        if not cohort_name or not isinstance(cohort_name, str):
            raise InvalidParameterError("Cohort name must be a non-empty string")
        
        try:
            return self.post(data={"cohort_name": cohort_name})
        except Exception as e:
            raise CohortError(f"Failed to create cohort: {str(e)}")

    def update(self, cohort_id, cohort_name):
        """
        Update a cohort's name
        
        Args:
            cohort_id (str): ID of the cohort to update
            cohort_name (str): New name for the cohort
            
        Returns:
            dict: Updated cohort object
            
        Raises:
            InvalidParameterError: If required parameters are missing or invalid
            CohortNotFoundError: If the cohort doesn't exist
            CohortError: If there's an error updating the cohort
        """
        if not cohort_id:
            raise InvalidParameterError("Cohort ID must be provided")
        if not cohort_name or not isinstance(cohort_name, str):
            raise InvalidParameterError("Cohort name must be a non-empty string")
        
        try:
            return self.put(f"{cohort_id}", data={"cohort_name": cohort_name})
        except Exception as e:
            if "404" in str(e):
                raise CohortNotFoundError(f"Cohort with ID {cohort_id} not found")
            raise CohortError(f"Failed to update cohort: {str(e)}")

    def add_user(self, cohort_id, user_id):
        """
        Add a user to a cohort
        
        Args:
            cohort_id (str): ID of the cohort
            user_id (str): ID of the user to add
            
        Returns:
            dict: Response confirming user addition
            
        Raises:
            InvalidParameterError: If required parameters are missing
            CohortNotFoundError: If the cohort doesn't exist
            UserNotFoundError: If the user doesn't exist
            CohortError: If there's an error adding the user
        """
        if not cohort_id or not user_id:
            raise InvalidParameterError("Both cohort_id and user_id must be provided")
        
        try:
            return self.post(f"{cohort_id}/add_user_to_cohort/", data={"user_id": user_id})
        except Exception as e:
            error_msg = str(e).lower()
            if "404" in error_msg and "cohort" in error_msg:
                raise CohortNotFoundError(f"Cohort with ID {cohort_id} not found")
            elif "404" in error_msg and "user" in error_msg:
                raise UserNotFoundError(f"User with ID {user_id} not found")
            raise CohortError(f"Failed to add user to cohort: {str(e)}")

    def remove_user(self, cohort_id, user_id):
        """
        Remove a user from a cohort
        
        Args:
            cohort_id (str): ID of the cohort
            user_id (str): ID of the user to remove
            
        Returns:
            dict: Response confirming user removal
            
        Raises:
            InvalidParameterError: If required parameters are missing
            CohortNotFoundError: If the cohort doesn't exist
            UserNotFoundError: If the user doesn't exist
            CohortError: If there's an error removing the user
        """
        if not cohort_id or not user_id:
            raise InvalidParameterError("Both cohort_id and user_id must be provided")
        
        try:
            return self.post(f"{cohort_id}/remove_user_from_cohort/", data={"user_id": user_id})
        except Exception as e:
            error_msg = str(e).lower()
            if "404" in error_msg and "cohort" in error_msg:
                raise CohortNotFoundError(f"Cohort with ID {cohort_id} not found")
            elif "404" in error_msg and "user" in error_msg:
                raise UserNotFoundError(f"User with ID {user_id} not found")
            raise CohortError(f"Failed to remove user from cohort: {str(e)}")

    def get_for_user(self, user_id):
        """
        Get all cohorts for a specific user
        
        Args:
            user_id (str): ID of the user to get cohorts for
            
        Returns:
            list: List of cohorts the user belongs to
            
        Raises:
            InvalidParameterError: If user_id is not provided
            UserNotFoundError: If the user doesn't exist
            CohortError: If there's an error fetching the cohorts
        """
        if not user_id:
            raise InvalidParameterError("User ID must be provided")
        
        try:
            return self.get("cohorts_for_user/", params={"user_id": user_id})
        except Exception as e:
            if "404" in str(e):
                raise UserNotFoundError(f"User with ID {user_id} not found")
            raise CohortError(f"Failed to fetch cohorts for user: {str(e)}") 