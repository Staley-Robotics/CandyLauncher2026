import typing

from commands2 import Command, Subsystem
from subsystems.SingleArmPivot import TalonFXSingleArmPivot

class LaunchSingleArm(Command):
    # Variable Declaration
    pivot_arm:TalonFXSingleArmPivot = None
    
    # Initialization
    def __init__( self,
                  pivot_arm:TalonFXSingleArmPivot,
                ) -> None:
        # Command Attributes
        self.pivot_arm:TalonFXSingleArmPivot = pivot_arm
        self.setName( "LaunchSingleArm" )
        self.addRequirements( pivot_arm )

    def initialize(self) -> None:
        pass

    def execute(self) -> None:
        self.pivot_arm.set_pivot_setpoint( TalonFXSingleArmPivot.Positions.MAX )

    def end(self, interrupted:bool) -> None:
        pass

    def isFinished(self) -> bool:
        return self.pivot_arm.get_at_setpoint()

    def runsWhenDisabled(self) -> bool:
        return False