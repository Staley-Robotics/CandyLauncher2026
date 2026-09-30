import typing

from commands2 import Command
from wpimath.units import degrees
from ntcore.util import ntproperty

from subsystems.SingleArmPivot import TalonFXSingleArmPivot

class PivotNTProperty(Command):
    # Variable Declaration
    pivot_arm:TalonFXSingleArmPivot = None
    set_pos = ntproperty("/Settings/PivotNTProperty/set_pos/",TalonFXSingleArmPivot.Positions.MIN, writeDefault = True)
    # Initialization
    def __init__( self,
                  pivot_arm:TalonFXSingleArmPivot,
                ) -> None:
        # Command Attributes
        self.pivot_arm:TalonFXSingleArmPivot = pivot_arm
        self.setName( f"PivotNTProperty: {self.set_pos} degrees" )
        self.addRequirements( pivot_arm )

    def initialize(self) -> None:
        pass
        # self.intake_sys.setPivotSetpoint(self.setPos)

    def execute(self) -> None:
        desired_set_pos = self.set_pos
        if self.set_pos > TalonFXSingleArmPivot.Positions.MAX:
            desired_set_pos = TalonFXSingleArmPivot.Positions.MAX
        elif self.set_pos < TalonFXSingleArmPivot.Positions.MIN:
            desired_set_pos = TalonFXSingleArmPivot.Positions.MIN
        self.pivot_arm.set_pivot_setpoint(desired_set_pos)

    def end(self, interrupted:bool) -> None:
        pass
        # if interrupted:
        # self.intake_sys.setPivotSetpoint(self.intake_sys.getPivotPosition())

    def isFinished(self) -> bool:
        return self.pivot_arm.get_at_setpoint()

    def runsWhenDisabled(self) -> bool:
        return False