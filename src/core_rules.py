"""
This module defines and tests standard automotive plastic trim design regulations (rib design, wall thickness variation, draft angles, and push-pin placement intervals).
"""



"""
Core Automotive Plastic Trim Engineering Rules Module.
Defines criteria for injection-molded components based on industry standards.
"""

class TrimDesignValidator:
    def __init__(self, nominal_wall_thickness: float):
        self.t = nominal_wall_thickness

    def validate_rib_thickness(self, rib_base_thickness: float) -> dict:
        """
        Validates rib thickness to prevent sink marks on the Class-A surface.
        Rule: Rib thickness should be between 50% and 60% of the nominal wall thickness.
        """
        min_allowed = 0.5 * self.t
        max_allowed = 0.6 * self.t
        is_valid = min_allowed <= rib_base_thickness <= max_allowed
        
        return {
            "parameter": "Rib Base Thickness",
            "value": rib_base_thickness,
            "limits": f"{min_allowed:.2f}mm - {max_allowed:.2f}mm",
            "status": "PASS" if is_valid else "FAIL_SINK_MARK_RISK"
        }

    def validate_draft_angle(self, feature_type: str, angle: float) -> dict:
        """
        Validates draft angles for surface release capabilities during tooling ejection.
        Rule: Nominal main surfaces require >= 3.0 deg. B-side features (ribs/bosses) require >= 0.5 deg.
        """
        min_angle = 3.0 if feature_type.lower() == "main_surface" else 0.5
        is_valid = angle >= min_angle
        
        return {
            "parameter": f"Draft Angle ({feature_type})",
            "value": f"{angle}°",
            "limits": f">= {min_angle}°",
            "status": "PASS" if is_valid else "FAIL_INSUFFICIENT_DRAFT"
        }

    def validate_doghouse_pushpin_spacing(self, distance_mm: float) -> dict:
        """
        Validates structural layout spacing for trim retainer retention pins.
        Rule: Spacing between push-pins should fall within standard assembly spans (150mm to 300mm).
        """
        is_valid = 150.0 <= distance_mm <= 300.0
        return {
            "parameter": "Retainer Pin Distance",
            "value": f"{distance_mm}mm",
            "limits": "150mm - 300mm",
            "status": "PASS" if is_valid else "FAIL_STRUCTURAL_DEFLECTION_RISK"
        }
      
