import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Statistics
import QuantConnect.Securities
import QuantConnect.Packets
import QuantConnect.Orders
import QuantConnect.Algorithm.Framework.Alphas
import QuantConnect
import datetime

class PacketType(System.Enum, System.IConvertible, System.IFormattable, System.IComparable):
    """
    Classifications of internal packet system
    
    enum PacketType, values: AlgorithmNode (1), AlgorithmStatus (12), AlphaHeartbeat (32), AlphaNode (30), AlphaResult (28), AlphaWork (29), AutocompleteResult (3), AutocompleteWork (2), BacktestError (11), BacktestNode (4), BacktestResult (5), BacktestWork (6), BuildError (15), BuildSuccess (14), BuildWork (13), CommandResult (23), Debug (19), DebuggingStatus (33), Documentation (26), DocumentationResult (25), GitHubHook (24), HandledError (17), History (22), LiveNode (7), LiveResult (8), LiveWork (9), Log (18), None (0), OrderEvent (20), RegressionAlgorithm (31), RuntimeError (16), SecurityTypes (10), Success (21), SystemDebug (27)
    """
    value__: int
    AlgorithmNode: 'PacketType'
    AlgorithmStatus: 'PacketType'
    AlphaHeartbeat: 'PacketType'
    AlphaNode: 'PacketType'
    AlphaResult: 'PacketType'
    AlphaWork: 'PacketType'
    AutocompleteResult: 'PacketType'
    AutocompleteWork: 'PacketType'
    BacktestError: 'PacketType'
    BacktestNode: 'PacketType'
    BacktestResult: 'PacketType'
    BacktestWork: 'PacketType'
    BuildError: 'PacketType'
    BuildSuccess: 'PacketType'
    BuildWork: 'PacketType'
    CommandResult: 'PacketType'
    Debug: 'PacketType'
    DebuggingStatus: 'PacketType'
    Documentation: 'PacketType'
    DocumentationResult: 'PacketType'
    GitHubHook: 'PacketType'
    HandledError: 'PacketType'
    History: 'PacketType'
    LiveNode: 'PacketType'
    LiveResult: 'PacketType'
    LiveWork: 'PacketType'
    Log: 'PacketType'
    OrderEvent: 'PacketType'
    RegressionAlgorithm: 'PacketType'
    RuntimeError: 'PacketType'
    SecurityTypes: 'PacketType'
    Success: 'PacketType'
    SystemDebug: 'PacketType'
    None_: 'PacketType'


class RuntimeErrorPacket(QuantConnect.Packets.Packet):
    """
    Algorithm runtime error packet from the lean engine. 
                This is a managed error which stops the algorithm execution.
    
    RuntimeErrorPacket()
    RuntimeErrorPacket(userId: int, algorithmId: str, message: str, stacktrace: str)
    """
    @typing.overload
    def __init__(self) -> QuantConnect.Packets.RuntimeErrorPacket:
        pass

    @typing.overload
    def __init__(self, userId: int, algorithmId: str, message: str, stacktrace: str) -> QuantConnect.Packets.RuntimeErrorPacket:
        pass

    def __init__(self, *args) -> QuantConnect.Packets.RuntimeErrorPacket:
        pass

    AlgorithmId: str
    Message: str
    StackTrace: str
    UserId: int

class SecurityTypesPacket(QuantConnect.Packets.Packet):
    """
    Security types packet contains information on the markets the user data has requested.
    
    SecurityTypesPacket()
    """
    TypesCSV: str

    Types: typing.List[QuantConnect.SecurityType]


class StatusHistoryResult(QuantConnect.Packets.HistoryResult):
    """
    Specifies the progress of a request
    
    StatusHistoryResult()
    StatusHistoryResult(progress: int)
    """
    @typing.overload
    def __init__(self) -> QuantConnect.Packets.StatusHistoryResult:
        pass

    @typing.overload
    def __init__(self, progress: int) -> QuantConnect.Packets.StatusHistoryResult:
        pass

    def __init__(self, *args) -> QuantConnect.Packets.StatusHistoryResult:
        pass

    Progress: int

class SystemDebugPacket(QuantConnect.Packets.DebugPacket):
    """
    Debug packets generated by Lean
    
    SystemDebugPacket()
    SystemDebugPacket(projectId: int, algorithmId: str, compileId: str, message: str, toast: bool)
    """
    @typing.overload
    def __init__(self) -> QuantConnect.Packets.SystemDebugPacket:
        pass

    @typing.overload
    def __init__(self, projectId: int, algorithmId: str, compileId: str, message: str, toast: bool) -> QuantConnect.Packets.SystemDebugPacket:
        pass

    def __init__(self, *args) -> QuantConnect.Packets.SystemDebugPacket:
        pass
