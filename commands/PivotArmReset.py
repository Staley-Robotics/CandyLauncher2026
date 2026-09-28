import typing

from commands2 import Command, Subsystem
from subsystems.ExampleSubsystem import ExampleSubsystem
from subsystems.SingleArmPivot import TalonFXSingleArmPivot

class ResetPivotArm(Command):
    # Variable Declaration
    pivot_arm:TalonFXSingleArmPivot = None
    
    # Initialization
    def __init__( self,
                  pivot_arm:Subsystem,
                ) -> None:
        # Command Attributes
        self.pivot_arm:TalonFXSingleArmPivot = pivot_arm
        
        self.setName( "ResetPivotArm" )
        self.addRequirements( pivot_arm )

    def initialize(self) -> None:
        pass
    def execute(self) -> None:
        self.pivot_arm.set_pivot_setpoint(self.pivot_arm.Positions.MIN)

    def end(self, interrupted:bool) -> None:
        pass

    def isFinished(self) -> bool:
        return self.pivot_arm.get_at_setpoint()

    def runsWhenDisabled(self) -> bool:
        return False
    
    