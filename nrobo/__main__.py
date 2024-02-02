"""
Entry point for nrobo-copy framework
"""

import sys

if __name__ == '__main__':
    # Trigger point for nrobo-copy command line utility
    from nrobo.cli import main

    sys.exit(main())