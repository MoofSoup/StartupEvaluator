from supabase import create_client
from dotenv import load_dotenv
import os
from pprint import pprint
from typing import Tuple, Dict, Any

# ANSI color codes for prettier output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    ENDC = '\033[0m'

def get_companies_dict() -> Tuple[bool, Dict[str, Any], str]:
    """
    Helper function to fetch companies from Supabase and format them as a dict.
    Returns: (success_bool, companies_dict, error_message)
    """
    try:
        # Load environment variables
        load_dotenv()
        SUPABASE_URL = os.getenv("SUPABASE_URL")
        SUPABASE_KEY = os.getenv("SUPABASE_KEY")

        if not SUPABASE_URL or not SUPABASE_KEY:
            return False, {}, "Missing environment variables"

        # Initialize Supabase client
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

        # Fetch companies
        response = supabase.table('Companies').select(
            'company_name,company_pitch,company_logo'
        ).execute()

        # Process companies into dict
        companies_dict = {}
        for company in response.data:
            # Create key from company name
            key = company['company_name'].lower().replace(' ', '_')
            
            # Create company entry
            companies_dict[key] = {
                "name": company['company_name'],
                "pitch": company['company_pitch'],
                "logo_url": company['company_logo']
            }
            
            print(f"{Colors.GREEN}✓ Processed {company['company_name']}{Colors.ENDC}")

        return True, companies_dict, ""

    except Exception as e:
        return False, {}, str(e)

if __name__ == "__main__":
    print(f"\n{Colors.BLUE}Fetching and formatting companies...{Colors.ENDC}")
    
    success, companies, error = get_companies_dict()
    
    if success:
        print(f"\n{Colors.BLUE}Generated dictionary:{Colors.ENDC}")
        pprint(companies)
        print(f"\n{Colors.GREEN}Successfully processed {len(companies)} companies{Colors.ENDC}")
    else:
        print(f"\n{Colors.RED}Error: {error}{Colors.ENDC}")