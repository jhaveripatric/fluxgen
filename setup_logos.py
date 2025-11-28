#!/usr/bin/env python3
"""
FluxGen Logo Setup Script
Copies logo files to the appropriate location in the Flask app static directory
"""

import shutil
from pathlib import Path

def setup_logos():
    """Copy logo files to the static/images directory"""
    
    # Define paths
    project_root = Path(__file__).parent
    repo_dir = project_root / 'repo' / 'app' / 'static' / 'images'
    
    # Source logos (you'll need to place these in the FluxGen root directory)
    source_full_logo = project_root / 'fluxgen.png'
    source_monogram = project_root / 'fluxgen-onlylogo_high_resolution.png'
    
    # Create destination directory if it doesn't exist
    repo_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy logos
    logos_copied = []
    
    if source_full_logo.exists():
        dest = repo_dir / 'fluxgen-logo-full.png'
        shutil.copy2(source_full_logo, dest)
        logos_copied.append(f"✓ Full logo: {dest}")
    else:
        print(f"⚠ Warning: {source_full_logo} not found")
    
    if source_monogram.exists():
        dest = repo_dir / 'fluxgen-logo-monogram.png'
        shutil.copy2(source_monogram, dest)
        logos_copied.append(f"✓ Monogram: {dest}")
    else:
        print(f"⚠ Warning: {source_monogram} not found")
    
    # Report results
    if logos_copied:
        print("\n" + "="*60)
        print("LOGO SETUP COMPLETE")
        print("="*60)
        for msg in logos_copied:
            print(msg)
        print(f"\nLogos available at: {repo_dir}")
        print("="*60)
    else:
        print("\n" + "="*60)
        print("ERROR: No logos found!")
        print("="*60)
        print("\nPlease ensure the following files exist in:")
        print(f"  {project_root}/")
        print("\n  1. fluxgen.png (full logo with text)")
        print("  2. fluxgen-onlylogo_high_resolution.png (monogram)")
        print("="*60)

if __name__ == '__main__':
    setup_logos()
