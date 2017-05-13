# coding: utf-8

"""
    Postmark API

    Postmark makes sending and receiving email incredibly easy. 

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InboundMessageFullDetailsResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, _from=None, from_name=None, from_full=None, to=None, to_full=None, cc=None, cc_full=None, reply_to=None, original_recipient=None, subject=None, date=None, mailbox_hash=None, text_body=None, html_body=None, tag=None, headers=None, attachments=None, message_id=None, blocked_reason=None, status=None):
        """
        InboundMessageFullDetailsResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            '_from': 'str',
            'from_name': 'str',
            'from_full': 'InboundMessageFullDetailsResponseFromFull',
            'to': 'str',
            'to_full': 'list[EmailNameAddressPair]',
            'cc': 'str',
            'cc_full': 'list[EmailNameAddressPair]',
            'reply_to': 'str',
            'original_recipient': 'str',
            'subject': 'str',
            'date': 'str',
            'mailbox_hash': 'str',
            'text_body': 'str',
            'html_body': 'str',
            'tag': 'str',
            'headers': 'HeaderCollection',
            'attachments': 'AttachmentCollection',
            'message_id': 'str',
            'blocked_reason': 'str',
            'status': 'str'
        }

        self.attribute_map = {
            '_from': 'From',
            'from_name': 'FromName',
            'from_full': 'FromFull',
            'to': 'To',
            'to_full': 'ToFull',
            'cc': 'Cc',
            'cc_full': 'CcFull',
            'reply_to': 'ReplyTo',
            'original_recipient': 'OriginalRecipient',
            'subject': 'Subject',
            'date': 'Date',
            'mailbox_hash': 'MailboxHash',
            'text_body': 'TextBody',
            'html_body': 'HtmlBody',
            'tag': 'Tag',
            'headers': 'Headers',
            'attachments': 'Attachments',
            'message_id': 'MessageID',
            'blocked_reason': 'BlockedReason',
            'status': 'Status'
        }

        self.__from = None
        self._from_name = None
        self._from_full = None
        self._to = None
        self._to_full = None
        self._cc = None
        self._cc_full = None
        self._reply_to = None
        self._original_recipient = None
        self._subject = None
        self._date = None
        self._mailbox_hash = None
        self._text_body = None
        self._html_body = None
        self._tag = None
        self._headers = None
        self._attachments = None
        self._message_id = None
        self._blocked_reason = None
        self._status = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if _from is not None:
          self._from = _from
        if from_name is not None:
          self.from_name = from_name
        if from_full is not None:
          self.from_full = from_full
        if to is not None:
          self.to = to
        if to_full is not None:
          self.to_full = to_full
        if cc is not None:
          self.cc = cc
        if cc_full is not None:
          self.cc_full = cc_full
        if reply_to is not None:
          self.reply_to = reply_to
        if original_recipient is not None:
          self.original_recipient = original_recipient
        if subject is not None:
          self.subject = subject
        if date is not None:
          self.date = date
        if mailbox_hash is not None:
          self.mailbox_hash = mailbox_hash
        if text_body is not None:
          self.text_body = text_body
        if html_body is not None:
          self.html_body = html_body
        if tag is not None:
          self.tag = tag
        if headers is not None:
          self.headers = headers
        if attachments is not None:
          self.attachments = attachments
        if message_id is not None:
          self.message_id = message_id
        if blocked_reason is not None:
          self.blocked_reason = blocked_reason
        if status is not None:
          self.status = status

    @property
    def _from(self):
        """
        Gets the _from of this InboundMessageFullDetailsResponse.

        :return: The _from of this InboundMessageFullDetailsResponse.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this InboundMessageFullDetailsResponse.

        :param _from: The _from of this InboundMessageFullDetailsResponse.
        :type: str
        """

        self.__from = _from

    @property
    def from_name(self):
        """
        Gets the from_name of this InboundMessageFullDetailsResponse.

        :return: The from_name of this InboundMessageFullDetailsResponse.
        :rtype: str
        """
        return self._from_name

    @from_name.setter
    def from_name(self, from_name):
        """
        Sets the from_name of this InboundMessageFullDetailsResponse.

        :param from_name: The from_name of this InboundMessageFullDetailsResponse.
        :type: str
        """

        self._from_name = from_name

    @property
    def from_full(self):
        """
        Gets the from_full of this InboundMessageFullDetailsResponse.

        :return: The from_full of this InboundMessageFullDetailsResponse.
        :rtype: InboundMessageFullDetailsResponseFromFull
        """
        return self._from_full

    @from_full.setter
    def from_full(self, from_full):
        """
        Sets the from_full of this InboundMessageFullDetailsResponse.

        :param from_full: The from_full of this InboundMessageFullDetailsResponse.
        :type: InboundMessageFullDetailsResponseFromFull
        """

        self._from_full = from_full

    @property
    def to(self):
        """
        Gets the to of this InboundMessageFullDetailsResponse.

        :return: The to of this InboundMessageFullDetailsResponse.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """
        Sets the to of this InboundMessageFullDetailsResponse.

        :param to: The to of this InboundMessageFullDetailsResponse.
        :type: str
        """

        self._to = to

    @property
    def to_full(self):
        """
        Gets the to_full of this InboundMessageFullDetailsResponse.

        :return: The to_full of this InboundMessageFullDetailsResponse.
        :rtype: list[EmailNameAddressPair]
        """
        return self._to_full

    @to_full.setter
    def to_full(self, to_full):
        """
        Sets the to_full of this InboundMessageFullDetailsResponse.

        :param to_full: The to_full of this InboundMessageFullDetailsResponse.
        :type: list[EmailNameAddressPair]
        """

        self._to_full = to_full

    @property
    def cc(self):
        """
        Gets the cc of this InboundMessageFullDetailsResponse.

        :return: The cc of this InboundMessageFullDetailsResponse.
        :rtype: str
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """
        Sets the cc of this InboundMessageFullDetailsResponse.

        :param cc: The cc of this InboundMessageFullDetailsResponse.
        :type: str
        """

        self._cc = cc

    @property
    def cc_full(self):
        """
        Gets the cc_full of this InboundMessageFullDetailsResponse.

        :return: The cc_full of this InboundMessageFullDetailsResponse.
        :rtype: list[EmailNameAddressPair]
        """
        return self._cc_full

    @cc_full.setter
    def cc_full(self, cc_full):
        """
        Sets the cc_full of this InboundMessageFullDetailsResponse.

        :param cc_full: The cc_full of this InboundMessageFullDetailsResponse.
        :type: list[EmailNameAddressPair]
        """

        self._cc_full = cc_full

    @property
    def reply_to(self):
        """
        Gets the reply_to of this InboundMessageFullDetailsResponse.

        :return: The reply_to of this InboundMessageFullDetailsResponse.
        :rtype: str
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, reply_to):
        """
        Sets the reply_to of this InboundMessageFullDetailsResponse.

        :param reply_to: The reply_to of this InboundMessageFullDetailsResponse.
        :type: str
        """

        self._reply_to = reply_to

    @property
    def original_recipient(self):
        """
        Gets the original_recipient of this InboundMessageFullDetailsResponse.

        :return: The original_recipient of this InboundMessageFullDetailsResponse.
        :rtype: str
        """
        return self._original_recipient

    @original_recipient.setter
    def original_recipient(self, original_recipient):
        """
        Sets the original_recipient of this InboundMessageFullDetailsResponse.

        :param original_recipient: The original_recipient of this InboundMessageFullDetailsResponse.
        :type: str
        """

        self._original_recipient = original_recipient

    @property
    def subject(self):
        """
        Gets the subject of this InboundMessageFullDetailsResponse.

        :return: The subject of this InboundMessageFullDetailsResponse.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this InboundMessageFullDetailsResponse.

        :param subject: The subject of this InboundMessageFullDetailsResponse.
        :type: str
        """

        self._subject = subject

    @property
    def date(self):
        """
        Gets the date of this InboundMessageFullDetailsResponse.

        :return: The date of this InboundMessageFullDetailsResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this InboundMessageFullDetailsResponse.

        :param date: The date of this InboundMessageFullDetailsResponse.
        :type: str
        """

        self._date = date

    @property
    def mailbox_hash(self):
        """
        Gets the mailbox_hash of this InboundMessageFullDetailsResponse.

        :return: The mailbox_hash of this InboundMessageFullDetailsResponse.
        :rtype: str
        """
        return self._mailbox_hash

    @mailbox_hash.setter
    def mailbox_hash(self, mailbox_hash):
        """
        Sets the mailbox_hash of this InboundMessageFullDetailsResponse.

        :param mailbox_hash: The mailbox_hash of this InboundMessageFullDetailsResponse.
        :type: str
        """

        self._mailbox_hash = mailbox_hash

    @property
    def text_body(self):
        """
        Gets the text_body of this InboundMessageFullDetailsResponse.

        :return: The text_body of this InboundMessageFullDetailsResponse.
        :rtype: str
        """
        return self._text_body

    @text_body.setter
    def text_body(self, text_body):
        """
        Sets the text_body of this InboundMessageFullDetailsResponse.

        :param text_body: The text_body of this InboundMessageFullDetailsResponse.
        :type: str
        """

        self._text_body = text_body

    @property
    def html_body(self):
        """
        Gets the html_body of this InboundMessageFullDetailsResponse.

        :return: The html_body of this InboundMessageFullDetailsResponse.
        :rtype: str
        """
        return self._html_body

    @html_body.setter
    def html_body(self, html_body):
        """
        Sets the html_body of this InboundMessageFullDetailsResponse.

        :param html_body: The html_body of this InboundMessageFullDetailsResponse.
        :type: str
        """

        self._html_body = html_body

    @property
    def tag(self):
        """
        Gets the tag of this InboundMessageFullDetailsResponse.

        :return: The tag of this InboundMessageFullDetailsResponse.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this InboundMessageFullDetailsResponse.

        :param tag: The tag of this InboundMessageFullDetailsResponse.
        :type: str
        """

        self._tag = tag

    @property
    def headers(self):
        """
        Gets the headers of this InboundMessageFullDetailsResponse.

        :return: The headers of this InboundMessageFullDetailsResponse.
        :rtype: HeaderCollection
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """
        Sets the headers of this InboundMessageFullDetailsResponse.

        :param headers: The headers of this InboundMessageFullDetailsResponse.
        :type: HeaderCollection
        """

        self._headers = headers

    @property
    def attachments(self):
        """
        Gets the attachments of this InboundMessageFullDetailsResponse.

        :return: The attachments of this InboundMessageFullDetailsResponse.
        :rtype: AttachmentCollection
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """
        Sets the attachments of this InboundMessageFullDetailsResponse.

        :param attachments: The attachments of this InboundMessageFullDetailsResponse.
        :type: AttachmentCollection
        """

        self._attachments = attachments

    @property
    def message_id(self):
        """
        Gets the message_id of this InboundMessageFullDetailsResponse.

        :return: The message_id of this InboundMessageFullDetailsResponse.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """
        Sets the message_id of this InboundMessageFullDetailsResponse.

        :param message_id: The message_id of this InboundMessageFullDetailsResponse.
        :type: str
        """

        self._message_id = message_id

    @property
    def blocked_reason(self):
        """
        Gets the blocked_reason of this InboundMessageFullDetailsResponse.

        :return: The blocked_reason of this InboundMessageFullDetailsResponse.
        :rtype: str
        """
        return self._blocked_reason

    @blocked_reason.setter
    def blocked_reason(self, blocked_reason):
        """
        Sets the blocked_reason of this InboundMessageFullDetailsResponse.

        :param blocked_reason: The blocked_reason of this InboundMessageFullDetailsResponse.
        :type: str
        """

        self._blocked_reason = blocked_reason

    @property
    def status(self):
        """
        Gets the status of this InboundMessageFullDetailsResponse.

        :return: The status of this InboundMessageFullDetailsResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this InboundMessageFullDetailsResponse.

        :param status: The status of this InboundMessageFullDetailsResponse.
        :type: str
        """

        self._status = status

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, InboundMessageFullDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other