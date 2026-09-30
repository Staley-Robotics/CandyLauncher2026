# Python Imports
from enum import Enum, auto

# FRC Imports
from wpilib import SendableChooser, SmartDashboard
from commands2 import Command, cmd

# Local Imports
from subsystems import ExampleSubsystem, SingleArmPivot
from commands import ExampleCommand, PivotNTProperty, PivotArmReset, LaunchSingleArm
from util import FalconXboxController

class ControlMode(Enum):
    TEST = auto()
    PRACTICE = auto()
    COMP = auto()
    DEMO = auto()
    

class RobotContainer:
    """
    RobotContainer is the Initial Container for an FRC Robot
    """
    __autoChooser:SendableChooser = SendableChooser()

    def __init__(self):
        """
        Initializes RobotContainer
        """
        ## Config
        control_mode = ControlMode.DEMO

        # Driver Controller
        self.driver1 = FalconXboxController( 0 )

        # Declare Subsystems
        launcher_arm = SingleArmPivot.TalonFXSingleArmPivot( 1, 2, -0.456055, False)

        # Commands
        self.pivot_to_ntproperty = PivotNTProperty.PivotNTProperty(launcher_arm)
        self.pivot_reset = PivotArmReset.ResetPivotArm(launcher_arm)
        self.launch = LaunchSingleArm.LaunchSingleArm(launcher_arm)
        # cmdSampleLeft = ExampleCommand(sysSample, driver1.getLeftX )
        # cmdSampleRight = ExampleCommand(sysSample, driver1.getRightX )

        # Default Commands
        # launcher_arm.setDefaultCommand( cmdSampleLeft )

        # Autonomous Chooser
        self.__autoChooser.setDefaultOption( "1 - None", cmd.none() )
        SmartDashboard.putData( "Autonomous Mode", self.__autoChooser )

        ## Setup Controls
        match control_mode:
            case ControlMode.TEST:
                self.setControlsTest()
            case ControlMode.PRACTICE:
                self.setControlsPractice()
            case ControlMode.COMP:
                self.setControlsComp()
            case ControlMode.DEMO:
                self.setControlsDemo()

    def setControlsTest(self):
        pass
    def setControlsPractice(self):
        pass
    def setControlsComp(self):
        pass
    def setControlsDemo(self):
        self.driver1.a().whileTrue(self.pivot_to_ntproperty)
        self.driver1.povDown().onTrue(self.pivot_reset)
        self.driver1.povUp().onTrue(self.launch)

    def getAutonomousCommand(self) -> Command:
        """
        Get the Autonomous Command that is currently selected in the AutoChooser Dropdown on the Shuffleboard / SmartDashboards
        """
        chooserValue = self.__autoChooser.getSelected()
        return chooserValue if isinstance( chooserValue, Command ) else cmd.none()
