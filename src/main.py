"""
The orchestration layer executing checking actions across design features and formatting data into a clear console display.
"""




"""
Main Execution Script for the Trim Engineering Suite.
"""
from core_rules import TrimDesignValidator
from bom_generator import BillOfMaterials

def run_suite():
    print("======================================================================")
    print("      MAHINDRA TRIMS COE - VIRTUAL GATEWAY DESIGN CHECK ENGINE")
    print("======================================================================\n")
    
    # Initialize design engine assuming a nominal trim thickness of 2.5mm
    validator = TrimDesignValidator(nominal_wall_thickness=2.5)
    
    # 1. Execute Engineering Rule Clearance Validations
    checks = [
        validator.validate_rib_thickness(rib_base_thickness=1.3),
        validator.validate_rib_thickness(rib_base_thickness=1.8),  # Will fail rule check
        validator.validate_draft_angle("main_surface", 3.5),
        validator.validate_draft_angle("ribs", 0.3),              # Will fail rule check
        validator.validate_doghouse_pushpin_spacing(220.0)
    ]
    
    print("--- DESIGN INTEGRITY CHECKS ---")
    for check in checks:
        print(f"[{check['status']}] {check['parameter']}: Value: {check['value']} | Allowed: {check['limits']}")
    
    # 2. Build the Product Assembly Bill of Materials (BOM)
    bom = BillOfMaterials()
    bom.add_component("M&M-7011-01", "Door Trim Main Substrate", "PP-TD20", 1.85, 1)
    bom.add_component("M&M-7011-02", "Integrated Map Pocket", "ABS", 0.42, 1)
    bom.add_component("M&M-7011-09", "Ergonomic Grab Handle", "PC+ABS", 0.28, 1)
    bom.add_component("M&M-FIX-055", "Trim Retainer Fastener Pins", "PA66", 0.002, 12)
    
    print("\n--- GENERATED VEHICLE MANUFACTURING BOM ---")
    print(bom.generate_report())

if __name__ == "__main__":
    run_suite()
  
